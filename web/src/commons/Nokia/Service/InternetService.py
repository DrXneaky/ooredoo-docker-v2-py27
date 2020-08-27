# -*- coding: cp1252 -*-

class HSIServices:
    def _init(self, PE, serviceid, rd, InterfaceName, IPAdress, PortID, Vlan, Authentication_Key, VpnDescription):
        self.PE = PE
        self.serviceid
        self.rd = rd
        self.InterfaceName = InterfaceName
        self.IPAdress
        self.PortID = PortID
        self.Vlan = Vlan
        self.Authentication_Key = Authentication_Key
        self.VpnDescription = VpnDescription

    ##    def _Static_VPN_Service:
    def _OSPF_Configure_HSI_loopback(self, loopback):
        var_HSI = """
            ==================

            configure service ies 9500 customer 4 create
                interface "loopback-HSI-OSPF" create
                    address %s
                    loopback
                exit

            configure router ospf
                area 0.0.0.0
                    interface "loopback-HSI-OSPF"
                        no shutdown
                    exit
                exit
            """ % (loopback)
        return var_HSI

    def _OSPF_HSI_Service(self, interfacename, interfacenamedescription, address, port, vlanHSI, qosingress, qosegress,
                          Areainterfacename, Authentication_Key):

        var_HSI = """
        ==================

        configure service ies 9500 customer 4 create
            description "INTERNET_SERVICE"
            interface "to_CPE_%s" create
                description "IV CEI;DT_FIXE;HSI_%s;INCLUDE_SC"
                address %s
                sap %s:%s create
                    ingress
                       qos %s
                    exit
                    egress
                       qos %s
                    exit
                    collect-stats
                    accounting-policy 10
                exit
            exit

                service-name "INTERNET_SERVICE"
                no shutdown
        exit
        ---------------------------------------------------------------------------------------

        configure router ospf
            area 0.0.0.2
                interface "to_CPE_%s"
                                interface-type point-to-point
                                mtu 1500
                                authentication-type message-digest
                                message-digest-key 1 md5 %s
                                no shutdown
                exit
            exit
        exit


    """ % (interfacename, interfacenamedescription, address, port, vlanHSI, qosingress, qosegress, Areainterfacename,
           Authentication_Key)
        return var_HSI

    ##

    def _Static_HSI_Service(self, interfacename, interfacenamedescription, IPPbaaddress, port, vlanHSI, qosingress,
                            qosegress, publicIP, IPCpeHSIAdress):

        var_HSI = """
        ==================


        configure service ies 9500 customer 4 create
                    description "INTERNET_SERVICE"
                    interface "to_CPE_%s" create
                        description "IV CEI;DT_FIXE;HSI_%s;INCLUDE_SC"
                        address %s
                        sap %s:%s create
                            ingress
                                qos %s
                            exit
                            egress
                                qos %s
                            exit
                            collect-stats
                            accounting-policy 10
                        exit
                    exit
                    service-name "INTERNET_SERVICE"
                    no shutdown
                exit

        static-route-entry %s next-hop %s
            no shutdown
            exit

        """ % (interfacename, interfacenamedescription, IPPbaaddress, port, vlanHSI, qosingress, qosegress, publicIP,
               IPCpeHSIAdress)
        return var_HSI

    def _Static_Cisco_HSI_Service(self, vlan_id, CLient_description, vlan, interface_description, autonomous_system,
                                  publicIPBGP, mask, OQS_Ingress, qos_egress, publicIP, mask_public, IPCpeHSIAdress,
                                  HSI_route_description):
        print("hello")
        # _CheckVLAN(vlan)
        # if _CheckVLAN == "FALSE":
        #     var_HSI = """
        #             vlan %s
        #              name HSI_%s
        #
        #             interface Vlan%s
        #              description IV CEI;DT_FIXE;HSI_%s;INCLUDE_SC;
        #              ip address %s %s
        #              no ip redirects
        #              no ip proxy-arp
        #              service-policy input Bandwidth_Limitation_%s
        #              service-policy outputBandwidth_Limitation_%s
        #             no shut
        #             !
        #
        #             router bgp %s
        #
        #               address-family ipv4
        #               network %s mask %s
        #               exit-address-family
        #
        #             ip route %s %s %s name HSI_%s
        #
        #               """ % (
        #     vlan_id, CLient_description, vlan, interface_description, autonomous_system, publicIPBGP, mask, OQS_Ingress,
        #     qos_egress, publicIP, mask_public, IPCpeHSIAdress, HSI_route_description)
        # else:
        #     print("raise_Alarm vlanHSI")
