class policy:
    
    def _main(self,policy):
        self.policy=policy


    def _filter_VOIP(self,VOIP_addr):
        
        VOIP_FILTER="""
            filter 
             match-list
             ip-prefix-list "CPM-OSPF"
                    prefix %s 

            exit
            """%(VOIP_addr)
        return VOIP_FILTER


    def _filter_HSI(self,HSI_addr):
        
        HSI_FILTER="""
            filter 
             match-list
             ip-prefix-list "CPM-OSPF"
                    prefix %s 

            exit
            """%(HSI_addr)
        return HSI_FILTER
    
    def _filter_VPN(self,VPN_addr):
        
        VPN_FILTER="""
            filter 
             match-list
             ip-prefix-list "CPM-OSPF"
                    prefix %s

            exit
            """%(VPN_addr)
        return VPN_FILTER

    def _filter_OM(self,OMaddr):
        OM_FILTER="""
            filter 
             match-list
             ip-prefix-list "CPM-OSPF"
                    prefix %s 

            exit
            """%(OMaddr)
        return OM_FILTER

    def _filter_public_HSI(self,check,public_HSI,instance):
        
        public_HSI_filter="""
            prefix-list "ospf-subnets-main"               
                prefix %s exact
            exit
            """%(public_HSI)
        check1=check._check_ospf_subnets_main(instance)
        if check1 == "FALSE":
            
            policy_ospf_import="""
            policy-statement "policy-ospf-import"
                entry 5
                    from
                        protocol ospf
                        prefix-list "ospf-subnets-main"
                    exit
                    action accept
                exit
            exit
            """
        else:
            policy_ospf_import=""
        public_HSI_filter=public_HSI_filter+"\n" + policy_ospf_import
        return public_HSI_filter


    def _from_LoopbackOM_policy(self,check,instance,loopbackOM):
        policy="""
        configure router policy-options
            begin
            """
        policy_LoopbackOM="""
            prefix-list "ospf-LoopbackOM"
                prefix %s exact
            exit
            """%(loopbackOM)

        check1=check._check_from_ServersOM_OSPF(instance)
        if check1 == "FALSE":          
            policy_OM_Servers="""
            prefix-list "OM-Servers"
                    prefix 10.220.0.0/24 exact
            exit
            """
        else:
            policy_OM_Servers=""

        
        policy=policy+policy_LoopbackOM+policy_OM_Servers
        policy=policy+"\n \t commit \n exit"
        return policy


    def _from_LoopbackOM_OSPF_policy(self,check,instance):
        check1=check._check_from_LoopbackOM_OSPF(instance)

        if check1 == "FALSE":
            policy_LoopbackOM="""    
            policy-statement "from_LoopbackOM-OSPF_to_BGPVPN"
                entry 10
                    from
                        protocol ospf
                        prefix-list "ospf-LoopbackOM"
                    exit
                    action accept
                    exit
                exit
                default-action reject
            exit
            """
        else:
            policy_LoopbackOM=""
        
        check2=check._check_from_ServersOM_OSPF(instance)
        if check2 == "FALSE":        
            policy_ServersOM="""    
            
            policy-statement "from_OM-BGPVPN_to_OSPF"    
                    entry 10
                    from
                        protocol bgp-vpn
                        prefix-list "OM-Servers"
                    exit
                    to
                        protocol ospf
                    exit
                    action accept
                    exit
                exit
                default-action reject
            exit		

            commit
            exit
        """
        else:
            policy_ServersOM=""
        policy=policy_LoopbackOM+"\n"+policy_ServersOM
        return policy




    def _from_Loopback_VOIP_OSPF_policy(self,check,instance,LoopbackVOIP):

        check1=check._check_from_LoopbackVOIP_OSPF(instance)
        
        if check1 == "FALSE":
                
            policy_LoopbackVOIP="""
            policy-options
                begin
                    prefix-list "ospf-LoopbackVOIP"
                        prefix %s exact
                    exit
                exit
            commit
                            

            policy-statement "from_LoopbackVOIP-OSPF_to_BGPVPN"
                    entry 10
                        from
                            protocol ospf
                            prefix-list "ospf-LoopbackVOIP"
                        exit
                        action accept
                        exit
                    exit
                    default-action reject
                    exit
            commit
        """%(LoopbackVOIP)
        else:
            policy_LoopbackVOIP="""
            policy-options
                begin
                    prefix-list "ospf-LoopbackVOIP"
                        prefix %s exact
                    exit
                commit
            exit
            """%(LoopbackVOIP)
                            
            
        check2=check._check_from_policy_SBC_FW(instance)
        if check2 == "FALSE":
            policy_SBC_FW="""
            policy-options
                begin
                prefix-list "SBC-FW"
                    prefix 10.207.135.35/32 exact
                    prefix 197.14.1.7/32 exact
                    prefix 197.14.1.9/32 exact
                exit
                policy-statement "from_SBC-BGPVPN_to_OSPF"    
                    entry 10
                        from
                            prefix-list "SBC-FW"
                        exit
                        to
                            protocol ospf
                        exit
                        action accept
                        exit
                    exit
                    default-action reject
                        exit		

                commit		
                exit
                """
        else:
            policy_SBC_FW=""
        policy=policy_LoopbackVOIP+"\n"+policy_SBC_FW
        return policy
