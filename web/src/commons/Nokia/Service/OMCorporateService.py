# -*- coding: cp1252 -*-
class OMServices:

    def _init(self,PE,serviceid,rd,InterfaceName,IPAdress,PortID,Vlan,Authentication_Key,VpnDescription):
     self.PE=PE
     self.serviceid
     self.rd=rd
     self.InterfaceName=InterfaceName
     self.IPAdress
     self.PortID=PortID
     self.Vlan=Vlan
     self.Authentication_Key=Authentication_Key
     self.VpnDescription= VpnDescription


    def New_OSPF_OM_Service(self,rd,interfacename,interfacenamedescription,address,port,vlanOM,Areainterfacename,Authentication_Key):

        var_OM="""
        ==================

        configure service vprn 5101 customer 2
            description "VPRN_OM_Corporate"
            autonomous-system 64882
            route-distinguisher 64882:5101%s
            auto-bind-tunnel
                resolution-filter
                    rsvp
                exit
                resolution filter
            exit
            vrf-target target:64882:5101
            interface "to_CPE_%s" create
                description "IV CEI;DT_FIXE;OM_%s;INCLUDE_SC"
                address %s
                sap %s:%s create
                    ingress
                    qos 10
                    exit
                    egress
                    qos 10
                    exit
                    collect-stats
                    accounting-policy 10
                exit
            exit

                ospf
                    export "from_OM-BGPVPN_to_OSPF"
                    import "from_LoopbackOM-OSPF_to_BGPVPN"
                    area 0.0.0.0
                    interface "to_CPE_%s"
                        interface-type point-to-point
                        mtu 1500
                        authentication-type message-digest
                        message-digest-key 1 md5 %s
                        no shutdown

                    exit
                exit
            exit
        exit


        """% (rd,interfacename,interfacenamedescription,address,port,vlanOM,Areainterfacename,Authentication_Key)
        return var_OM
##
    def Old_OSPF_OM_Service(self,interfacename,interfacenamedescription,address,port,vlanOM,Areainterfacename,Authentication_Key):

        var_OM="""
        ==================

        configure service vprn 5101 customer 2

            interface "to_CPE_%s" create
                description "IV CEI;DT_FIXE;OM_%s;INCLUDE_SC"
                address %s
                sap %s:%s create
                    ingress
                    qos 10
                    exit
                    egress
                    qos 10
                    exit
                    collect-stats
                    accounting-policy 10
                exit
            exit

                ospf
                    export "from_OM-BGPVPN_to_OSPF"
                    import "from_LoopbackOM-OSPF_to_BGPVPN"
                    area 0.0.0.0
                        interface "to_CPE_%s"
                            interface-type point-to-point
                            mtu 1500
                            authentication-type message-digest
                            message-digest-key 1 md5 %s
                            no shutdown

                        exit
                    exit
                exit
            exit
        exit


        """% (interfacename,interfacenamedescription,address,port,vlanOM,Areainterfacename,Authentication_Key)
        return var_OM
##


    def _Static_OM_Service(self,interfacename,interfacenamedescription,IPPbaaddress,port,vlanOM,loopbackOM,IPOMCpeAdress):

        var_OM="""
        ==================
        configure service vprn 5101  customer 4 create
            description "VPRN_OM_Corporate"
                    interface "to_CPE_%s" create
                        description "IV CEI;DT_FIXE;OM_{{ }};INCLUDE_SC"
                        address %s
                        sap %s:%s create
                            ingress
                                qos 10
                            exit
                            egress
                                qos 10
                            exit
                            collect-stats
                            accounting-policy 10
                        exit
                    exit
                    service-name "OM_Corporate"
                    no shutdown
                exit

        static-route-entry %s
            next-hop %s
                no shutdown
            exit
        exit


        """% (interfacename,interfacenamedescription,IPPbaaddress,port,vlanOM,loopbackOM,IPOMCpeAdress)
        return var_OM

    def _Static_Cisco_OM_Service(self,vlan_id,CLient_description,vlan,interface_description,autonomous_system,IPPbaaddress,mask,loopbackOM,IPOMCpeAdress,static_route_description):
        _Check_Vlan(vlan)
        if _Check_Vlan == "FALSE":
            var_OM="""
                vlan %s
                 name OM_%s

                interface Vlan%s
                 description IV CEI;DT_FIXE;OM_%s;INCLUDE_SC;
                 ip vrf forwarding OM_Corporate
                 ip address %s %s ###
                 no ip redirects
                 no ip proxy-arp
                no shut
                !

                router bgp %s

                  address-family ipv4 vrf OM_Corporate
                  network %ds mask %s
                  exit-address-family

                ip route vrf OM_Corporate %s 255.255.255.255 %s name OM_%s

                  """%(vlan_id,CLient_description,vlan,interface_description,autonomous_system,IPPbaaddress,mask,loopbackOM,IPOMCpeAdress,static_route_description)
        else:
            raise_Alarm("vlanOM")
