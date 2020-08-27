# coding=utf-8
class VPNServices:

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

##    def _Static_VPN_Service:

    def _OSPF_New_VPN_Service(self,serviceid,Interface_Name_description,rd,Interface_Name,description,IPpbaVPN,port,vlanVPN,qos_ingress,qos_egress,OSPF_Interface_Name,Authentication_Key,VpnDescription):

        var_VPN="""
        ==================

        configure service vprn %s customer 2 create
            description "VPRN_%s"
            autonomous-system 64882
            route-distinguisher 64882:%s
            auto-bind-tunnel
                        resolution-filter
                            rsvp
                        exit
                        resolution filter
                    exit
            vrf-target target:64882:5101
            interface "to_CPE_%s" create
                description "IV CEI;DT_FIXE;VPN_%s;INCLUDE_SC"
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
            ospf
                export "from-BGPVPN-to-OSPF"
                area 0.0.0.0
                    interface "to_CPE_%s
                        interface-type point-to-point
                        mtu 1500
                        authentication-type message-digest
                        message-digest-key 1 md5 %s
                    exit
                exit
            exit

        service-name "VPRN_%s"
        no shutdown
        exit

    """% (serviceid,Interface_Name_description,rd,Interface_Name,description,IPpbaVPN,port,vlanVPN,qos_ingress,qos_egress,OSPF_Interface_Name,Authentication_Key,VpnDescription)
        return var_VPN
##
    def _OSPF_Old_VPN_Service(self,Serviceid,Interface_Name,description,IPpbaVPN,port,vlanVPN,qos_ingress,qos_egress,OSPF_interface_name,Authentication_Key):
        var_VPN="""
        ==================

        configure service vprn %s customer 2 create
            interface "to_CPE_%s" create
                description "IV CEI;DT_FIXE;VPN_%s;INCLUDE_SC"
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
            ospf
                export "from-BGPVPN-to-OSPF"
                area 0.0.0.0
                    interface "to_CPE_BNA_%s"
                        interface-type point-to-point
                        mtu 1500
                        authentication-type message-digest
                        message-digest-key 1 md5 %s
                    exit
                exit
            exit

        exit

        """% (Serviceid,Interface_Name,description,IPpbaVPN,port,vlanVPN,qos_ingress,qos_egress,OSPF_interface_name,Authentication_Key)
        return var_VPN


    def _STATIC_Old_VPN_Service(self,serviceid,Interface_Name,description,IPpbaVPN,port,vlanVPN,Authentication_Key,routes,IPVPNCpeAdress):

        var_VPN="""
        ==================

        configure service vprn %s customer 2 create
            interface "to_CPE_%s" create
                description "IV CEI;DT_FIXE;VPN_%s;INCLUDE_SC"
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
        %s

        exit

        """% (serviceid,Interface_Name,description,IPpbaVPN,port,vlanVPN,Authentication_Key)
        var_VPN=var_VPN + self.VPN_Nokia_IP_route(routes,IPVPNCpeAdress)

        return var_VPN

    def _STATIC_New_VPN_Service(self,serviceid,Interface_Name_description,rd,Interface_Name,description,IPpbaVPN,port,vlanVPN,Authentication_Key,routes,IPVPNCpeAdress):

        var_VPN="""
        ==================

        configure service vprn %s customer 2 create
            description "VPRN_%s"
            autonomous-system 64882
            route-distinguisher 64882:%srrr
            auto-bind-tunnel
                        resolution-filter
                            rsvp
                        exit
                        resolution filter
                    exit
            interface "to_CPE_%s" create
                description "IV CEI;DT_FIXE;VPN_%s;INCLUDE_SC"
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
        %s

        exit

        """% (serviceid,Interface_Name,description,IPpbaVPN,port,vlanVPN,Authentication_Key)
        var_VPN=var_VPN +self.VPN_Cisco_IP_route(routes,IPVPNCpeAdress)

        return var_VPN

    def _Static_Cisco_VPN_Service(self,vlan_id,CLient_description,vlan,interface_description,vrf_Name,address,qos_ingress,qos_egress,autonomous_system,bgp_vrf_name,publicIP,routes,IPVPNCpeAdress):
        _Check_Vlan(vlan)
        if _Check_Vlan == "FALSE":
            var_VPN="""
                vlan %s
                 name VPN_%s

                interface Vlan%s
                 description IV CEI;DT_FIXE;VPN_%s;INCLUDE_SC;
                 ip vrf forwarding %s
                 ip address %s
                 no ip redirects
                 no ip proxy-arp
                 service-policy qos_ingress
                 service-policy qos_egress
                no shut
                !

                router bgp %s

                  address-family ipv4 vrf %s
                  network %s
                  exit-address-family
                  """%(vlan_id,CLient_description,vlan,interface_description,vrf_Name,address,qos_ingress,qos_egress,autonomous_system,bgp_vrf_name,publicIP,routes,IPVPNCpeAdress)

            var_VPN=var_VPN+"\n"+self.VPN_Cisco_IP_route(routes,IPVPNCpeAdress)

        else:
            raise_Alarm("vlanVPN")
            var_VPN=""
        return var_VPN

    def VPN_Cisco_IP_route(self,routes,IPVPNCpeAdress,VPN_route_description):
        route=[]
        ip_route="hello"
        route=routes.split(";")
        for route_list in route:
            var_ip_route="""ip route vrf %s %s %s name VPN_%s"""%(route_list,VPN_route_description)
            ip_route=ip_route +"\n"+var_ip_route
        return ip_route
#
    def VPN_Nokia_IP_route(self,routes,IPVPNCpeAdress):

        ip_route=" "
        print(routes)
        route=routes.split(";")
        for route_list in route:

            var_VPN="""
                static-route-entry %s next-hop %s
                    no shutdown
                exit

            """% (route_list,IPVPNCpeAdress)

            ip_route=ip_route+"\n"+var_VPN
        return ip_route
#
#     def Create_New_VRF(self,VRF_Name,rd,serviceid,SW_Name):
#
#         var_VPN="""
#         ==================
#
#             SW%s_A
#             ===========
#
#
#             ip vrf VPN_%s
#              description VPN_%s
#              rd %s:%s
#             !
#             vlan %s
#              name TRANS_VRF_BNA_VPN_SW_DB
#             exit
#
#              vlan %s
#              name TRANS_VRF_BNA_VPN_ALU_A
#              exit
#
#             interface Vlan%s
#              description IV CEI;TRANS;VPN_BNA_SW900XDB;INCLUDE_SC;
#              ip vrf forwarding VPN_%s
#              ip address %s 255.255.255.252
#             no ip redirects
#              no ip proxy-arp
#              no shut
#             !
#             interface Vlan%s
#              description IV CEI;TRANS;VPN_BNA_ALU_A;INCLUDE_SC;
#              ip vrf forwarding VPN_%s
#              ip address %S 255.255.255.252
#              no ip redirects
#              no ip proxy-arp
#              no shut
#             !
#
#             interface Port-channel1
#
#              switchport trunk allowed vlan add %s
#              exit
#
#              interface Port-channel2  ### dans tous les switchs c'est int Po2 sauf à SW Manouba=  int vlan sous Po8 et à Sousse= subinterface int Po20.<vlan-id>  ###
#
#              switchport trunk allowed vlan add %s
#              exit
#
# (vrf_Name,vrf_Name,rd,serviceid,Back_Back_vlan,To_Nokia_vlan,Back_Back_vlan,vrf_Name,Back_Back_address,To_Nokia_vlan,vrf_Name,To_Nokia_address,Back_Back_vlan,To_Nokia_vlan,AS,vrf_Name,)
#             router bgp %s
#              !
#              address-family ipv4 vrf VPN_%s
#               no synchronization
#               redistribute static
#               neighbor CE-IBGP-VPN_% peer-group
#               neighbor CE-IBGP-VPN_%s remote-as %s
#               neighbor CE-IBGP-VPN_%s description --- IBGP peering to SW_900X_DB ---
#               neighbor CE-IBGP-VPN_% timers 7 21
#               neighbor CE-IBGP-VPN_%s send-community
#               neighbor CE-IBGP-VPN_%s next-hop-self
#               neighbor PE-EBGP-ALU-VPN_%s peer-group
#               neighbor PE-EBGP-ALU-VPN_%s remote-as 64882
#               neighbor PE-EBGP-ALU-VPN_%s description --- EBGP peering to Backbone-ALU  ---
#               neighbor PE-EBGP-ALU-VPN_%s timers 7 21
#               neighbor PE-EBGP-ALU-VPN_%s send-community
#               neighbor %s peer-group PE-EBGP-ALU-VPN_%s
#               neighbor %s activate
#               neighbor %s peer-group CE-IBGP-VPN_%s
#               neighbor %s activate
#              exit-address-family
#             !
#
#
#             exit
#
#             SW%s_B
#             =============
#
#             ip vrf VPN_%s
#              description VPN_%s
#              rd %s:51%s
#             !
#             vlan %
#              name TRANS_VRF_%s_VPN_SW_DA
#              exit
#
#             vlan %s
#              name TRANS_VRF_%s_VPN_ALU_B
#              exit
#
#             !
#             interface Vlan%s
#              description IV CEI;DT_FIXE;VPN_Y_SW900xDA;INCLUDE_SC;
#              ip vrf forwarding VPN_%s
#              ip address %s 255.255.255.252
#              no ip redirects
#              no ip proxy-arp
#              no shut
#             !
#             interface Vlan%s
#              description IV CEI;DT_FIXE;VPN_Y_ALU_B;INCLUDE_SC;
#              ip vrf forwarding VPN_%s
#              ip address %s 255.255.255.252
#              no ip redirects
#              no ip proxy-arp
#              no shut
#             !
#
#             interface Port-channel1
#
#              switchport trunk allowed vlan add %s
#              exit
#
#              interface Port-channel2
#
#              switchport trunk allowed vlan add %s
#              exit
#
#
#
#             router bgp %s
#              !
#              address-family ipv4 vrf VPN_%s
#               no synchronization
#               redistribute static
#               neighbor CE-IBGP-VPN_% peer-group
#               neighbor CE-IBGP-VPN_%s remote-as 6520X
#               neighbor CE-IBGP-VPN_%s description --- IBGP peering to SW_900X_DB ---
#               neighbor CE-IBGP-VPN_% timers 7 21
#               neighbor CE-IBGP-VPN_%s send-community
#               neighbor CE-IBGP-VPN_%s next-hop-self
#               neighbor PE-EBGP-ALU-VPN_%s peer-group
#               neighbor PE-EBGP-ALU-VPN_%s remote-as 64882
#               neighbor PE-EBGP-ALU-VPN_% description --- EBGP peering to Backbone-ALU  ---
#               neighbor PE-EBGP-ALU-VPN_%s timers 7 21
#               neighbor PE-EBGP-ALU-VPN_%s send-community
#               neighbor %s peer-group PE-EBGP-ALU-VPN_%s
#               neighbor %s activate
#               neighbor %s peer-group CE-IBGP-VPN_%s
#               neighbor %s activate
#              exit-address-family
#             !
#
#             PE%s_A
#             ==========
#
#
#             configure service vprn %s customer 1 create
#                         description "VPRN_VPN_%s"
#                         autonomous-system 64882
#                         route-distinguisher 64882:%s%s
#                         auto-bind rsvp-te
#                         vrf-target target:64882:%s
#                         interface "to_Cisco_Data_A" create
#                             description "to Cisco Switch Data A"
#                             address 10.20X.33.b+1/30
#                             sap lag-25:%s create #### généralement c'est lag-25 sauf à PE9002-A c'est lag-27###
#                                 ingress
#                                     qos 10
#                                 exit
#                                 egress
#                                     qos 10
#                                 exit
#                                 collect-stats
#                                 accounting-policy 10
#                             exit
#                         exit
#                         bgp
#                             export "export_to_bgp"
#                             local-as 64882
#                             enable-peer-tracking
#                             group "ce_cisco"
#                                 keepalive 7
#                                 hold-time 21
#                                 type external
#                                 neighbor %s
#                                     peer-as %s
#                                 exit
#                             exit
#                             no shutdown
#                         exit
#                         service-name "VPRN_VPN_%s"
#                         no shutdown
#
#
#             ---------------------------
#               filter
#                     match-list
#             		 ip-prefix-list "CPM-EBGP-NEIGHBOR"
#
#             		 prefix %s
#             		 exit
#             ----------------------------
#
#
#
#
#             PE%s_B
#             ==========
#
#             configure service vprn %s customer 1 create
#                         description "VPRN_VPN_%s"
#                         autonomous-system 64882
#                         route-distinguisher 64882:%s%s
#                         auto-bind rsvp-te
#                         vrf-target target:64882:%s
#                         interface "to_Cisco_Data_B" create
#                             description "to Cisco Switch Data B"
#                             address %s
#                             sap lag-25:%s create ### Dans tous les PE c'est lag-25 sauf à PE9148-B c'est lag-26 et à PE9002-B c'est lag-27###
#                                 ingress
#                                     qos 10
#                                 exit
#                                 egress
#                                     qos 10
#                                 exit
#                                 collect-stats
#                                 accounting-policy 10
#                             exit
#                         exit
#                         bgp
#                             export "export_to_bgp"
#                             local-as 64882
#                             enable-peer-tracking
#                             group "ce_cisco"
#                                 keepalive 7
#                                 hold-time 21
#                                 type external
#                                 neighbor %s
#                                     peer-as %s
#                                 exit
#                             exit
#                             no shutdown
#                         exit
#                         service-name "VPRN_VPN_%s"
#                         no shutdown
#
#
#             -------------
#               filter
#                     match-list
#             		 ip-prefix-list "CPM-EBGP-NEIGHBOR"
#
#             		 prefix  %s
#             		 exit
#             -----------------------
#             """%()
