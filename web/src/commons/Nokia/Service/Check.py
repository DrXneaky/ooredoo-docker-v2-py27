class Check:
    def _init_(self,Service):
        self.Service=Service

    def _CheckServiceExistance(self,serviceid,instance):
        Output=instance.send_command('show service service-using | match '+serviceid+' context all')
        Service=Output.split(" ")
        if serviceid == str(Service[0].strip()):
            return "TRUE"
        else:
            return "FALSE"


##    def _CheckServiceRoutingType(self,instance):

    def _CheckInterfaceExistance(self,instance,serviceid,interfacename):
        Output=instance.send_command('show router '+serviceid+' interface '+interfacename+ ' | match  \"Interfaces :"')
        if "Interfaces :" in Output:
            return "TRUE"
        else:
            return "FALSE"

##
##
    def _CheckAdressExistance(self,instance,serviceid,address):

        Output=instance.send_command('show router '+ serviceid +' route-table '+ address + ' longer | match \"No. of Routes:\"')
        if "No. of Routes:" in Output:
            return "TRUE"
        else:
            return "FALSE"

    def _CheckVLAN(self,instance,port,vlan):
        Output=instance.send_command('show service sap-using | match '+ port+':'+vlan)
        sap=port+":"+vlan
        if sap in Output:
            return "TRUE"
        else:
            return "FALSE"


    def _checkQOS(self,instance,QOS):
        if QOS<100:
            QOS="10"+str(QOS)
        elif QOS<1000:
            QOS="1"+str(QOS)

        Output=instance.send_command('show qos sap-ingress | match '+ QOS)
        if QOS in Output:
            return "TRUE"
        else:
            return "FALSE"

    def _Check_HSI_loopback(self,instance):
        Output=instance.send_command('admin display-config | match loopback-HSI-OSPF max-count 1 ')
        if "loopback-HSI-OSPF1" in Output:
            return "TRUE"
        else:
            return "FALSE"

    def _check_ospf_subnets_main(self,instance):
        Output=instance.send_command('admin display-config | match ospf-subnets-main max-count 1 ')
        if "ospf-subnets-main" in Output:
            return "TRUE"
        else:
            return "FALSE"


    def _check_from_LoopbackOM_OSPF(self,instance):
        Output=instance.send_command('admin display-config | match ospf-LoopbackOM max-count 1 ')
        if "ospf-LoopbackOM" in Output:
            return "TRUE"
        else:
            return "FALSE"
    def _check_from_ServersOM_OSPF(self,instance):
        Output=instance.send_command('admin display-config | match OM-Servers max-count 1 ')
        if "OM-Servers" in Output:
            return "TRUE"
        else:
            return "FALSE"

    def _check_from_LoopbackVOIP_OSPF(self,instance):

        Output=instance.send_command('admin display-config | match ospf-LoopbackVOIP max-count 1 ')
        if "ospf-LoopbackVOIP" in Output:
            return "TRUE"
        else:
            return "FALSE"

    def _check_from_policy_SBC_FW(self,instance):
        Output=instance.send_command('admin display-config | match SBC-FW max-count 1 ')
        if "SBC-FW" in Output:
            return "TRUE"
        else:
            return "FALSE"
