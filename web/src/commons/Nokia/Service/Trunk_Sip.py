class TrunkSipServices:

    def _init(self,PE):
         self.PE=PE


    def _OSPF_old_Static_VOIP_Service(self,interfacename,interfacenamedescription,address,port,vlanVOIP):
        var_VOIP="""

        ==================
        configure service vprn 5061

           interface "to_CPE_%s"  create
                description "IV CEI;DT_FIXE;VOIP_%s;INCLUDE_SC"
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
        exit
        """%(interfacename,interfacenamedescription,address,port,vlanVOIP)
        return var_VOIP

    def _OSPF_New_Static_VOIP_Service(self,rd,interfacenamedescription,address,port,vlanVOIP):

        var_VOIP="""
        configure service vprn 5061 customer 2 create
           description "VPRN_VoIP-Fixe"
           autonomous-system 64882
           route-distinguisher 64882:5061%s
                auto-bind-tunnel
                     resolution-filter
                          rsvp
                     exit
                     resolution filter
                exit

           vrf-target target:64882:5061
           interface "to_CPE_%s"  create
           description "IV CEI;DT_FIXE;VOIP_%s;INCLUDE_SC"
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

        service-name %s
        no shutdown
        exit

        """%(rd,interfacenamedescription,address,port,vlanVOIP)
        return var_VOIP

    def _OSPF_Old_OSPF_VOIP_Service(self,interfacename,interfacenamedescription,address,port,vlanVOIP):

        VAR_VOIP="""

        configure service vprn 5061
           interface "to_CPE_%s" create
                description "IV CEI;DT_FIXE;VOIP_%s;INCLUDE_SC"
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
        exit

        """% (interfacename,interfacenamedescription,address,port,vlanVOIP)
        return  VAR_VOIP


    def _OSPF_New_OSPF_VOIP_Service(self,rd,interfacename,interfacenamedescription,address,port,vlanVOIP,OSPFinterfacenamedescription,Authentication_Key):

        VAR_VOIP="""
        configure service vprn 5061 customer 2 create
           description "VPRN_VoIP-Fixe"
           autonomous-system 64882
           route-distinguisher 64882:5061%s
                auto-bind-tunnel
                     resolution-filter
                          rsvp
                     exit
                     resolution filter
                exit
           vrf-target target:64882:5061
           interface "to_CPE_%s" create
                description "IV CEI;DT_FIXE;VOIP_%s;INCLUDE_SC"
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
                export "from_SBC-BGPVPN_to_OSPF"
                import "from_LoopbackVOIP-OSPF_to_BGPVPN"
                area 0.0.0.0
                     interface "to_CPE_%s"
                          interface-type point-to-point
                          mtu 1500
                          authentication-type message-digest
                          message-digest-key 1 md5 "%s"
                          no shutdown
                          exit
                     exit
                exit
           exit

           service-name "VPRN_VoIP-Fixe"
           no shutdown
           """% (rd,interfacename,interfacenamedescription,address,port,vlanVOIP,interfacename,Authentication_Key)
        return VAR_VOIP

#     def _Static_Cisco_VOIP_Service(self,vlan_id,CLient_description,vlan,interface_description,address):
# #        _Check_Vlan(vlan)
#         if _Check_Vlan == "FALSE":
#             var_VOIP="""
#                 vlan %s
#                  name VOIP_%s
#
#                 interface Vlan%s
#                  description IV CEI;DT_FIXE;VOIP_%s;INCLUDE_SC;
#                  ip vrf forwarding Voix_Fixe
#                  ip address %s
#                  no ip redirects
#                  no ip proxy-arp
#                  service-policy input Policy_Trust
#                 !
#
#
#                   """%(vlan_id,CLient_description,vlan,interface_description,address)
#         else:
#             raise_Alarm("vlanVOIP")
#         return var_VOIP
