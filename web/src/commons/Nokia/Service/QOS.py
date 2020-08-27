class qos:
    
    def _init_(self,qos_value1):
        self.qos_value1=qos_value1

    def _Get_Bandwith(self,check,QOS,BANDWITH):
        qos_lis=[]
        if check._checkQOS == "FALSE":
            QOS=qos()
            qos_ingress=QOS._Create_Qos_ingress(BANDWITH)
            qos_egress=QOS._Create_Qos_egress(BANDWITH)
            qos_lis.append(qos_ingress)
            qos_lis.append(qos_egress)
           
        else:
            QOS=qos()
            qos_ingress=QOS._Get_Qos(BANDWITH)
            qos_egress=qos_ingress
            qos_lis.append(qos_ingress)
            qos_lis.append(qos_egress)
        return qos_lis


    def _Get_Qos(self,qos_value):
        if qos_value <10:
            qos_value="100"+str(qos_value)
            return str(qos_value)            
        elif qos_value < 100 and qos_value >= 10 :
            qos_value="10"+str(qos_value)
            return str(qos_value)
        elif qos_value < 1000 and qos_value >= 100 :
            qos_value="1"+str(qos_value)
            return str(qos_value)
        

    def _Create_Qos_ingress(self,qos_value):
        
        if qos_value < 100 and qos_value >= 10 :
            qos_value="0"+qos_value
        elif qos_value < 10:
            qos_value="00"+qos_value

            
        var_qos="""

        qos-ingress
        =====

        sap-ingress 1%s create
                    description "DSCP Marked Traffic and rate limiting for B2B clients"
                    queue 1 create
                        rate %s000
                    exit
                    queue 3 create
                        rate %s000
                    exit
                    queue 4 create
                        rate %s000
                    exit
                    queue 5 create
                        rate %s000
                    exit
                    queue 6 create
                        rate %s000
                    exit
                    queue 8 create
                        rate %s000
                    exit
                    queue 11 multipoint create
                    exit
                    fc "af" create
                        queue 3
                    exit
                    fc "be" create
                        queue 1
                    exit
                    fc "ef" create
                        queue 6
                    exit
                    fc "h2" create
                        queue 5
                    exit
                    fc "l1" create
                        queue 4
                    exit
                    fc "nc" create
                        queue 8
                    exit
                    dscp be fc "be" priority low
                    dscp ef fc "ef" priority high
                    dscp nc1 fc "nc" priority high
                    dscp nc2 fc "nc" priority high
                    dscp af11 fc "af" priority high
                    dscp af12 fc "af" priority low
                    dscp af13 fc "af" priority low
                    dscp af21 fc "l1" priority high
                    dscp af22 fc "l1" priority low
                    dscp af23 fc "l1" priority low
                    dscp af31 fc "l1" priority high
                    dscp af32 fc "l1" priority low
                    dscp af33 fc "l1" priority low
                    dscp af41 fc "h2" priority high
                    dscp af42 fc "h2" priority low
                    dscp af43 fc "h2" priority low
                exit
        """%(qos_value,qos_value,qos_value,qos_value,qos_value,qos_value,qos_value,qos_value,qos_value,qos_value,qos_value,qos_value,qos_value,qos_value)

        return var_qos

    def _Create_Qos_egress(self,qos):

        if qos < 100 and qos >10:
            qos_value="0"+qos
        elif qos<10:
            qos_value="00"+qos

            
        var_qos="""

        qos-egress
        =====

        sap-ingress 1%s create
                    description "DSCP Marked Traffic and rate limiting for B2B clients"
                    queue 1 create
                        rate %s000
                    exit
                    queue 3 create
                        rate %s000
                    exit
                    queue 4 create
                        rate %s000
                    exit
                    queue 5 create
                        rate %s000
                    exit
                    queue 6 create
                        rate %s000
                    exit
                    queue 8 create
                        rate %s000
                    exit
                    queue 11 multipoint create
                    exit
                    fc "af" create
                        queue 3
                    exit
                    fc "be" create
                        queue 1
                    exit
                    fc "ef" create
                        queue 6
                    exit
                    fc "h2" create
                        queue 5
                    exit
                    fc "l1" create
                        queue 4
                    exit
                    fc "nc" create
                        queue 8
                    exit
                    dscp be fc "be" priority low
                    dscp ef fc "ef" priority high
                    dscp nc1 fc "nc" priority high
                    dscp nc2 fc "nc" priority high
                    dscp af11 fc "af" priority high
                    dscp af12 fc "af" priority low
                    dscp af13 fc "af" priority low
                    dscp af21 fc "l1" priority high
                    dscp af22 fc "l1" priority low
                    dscp af23 fc "l1" priority low
                    dscp af31 fc "l1" priority high
                    dscp af32 fc "l1" priority low
                    dscp af33 fc "l1" priority low
                    dscp af41 fc "h2" priority high
                    dscp af42 fc "h2" priority low
                    dscp af43 fc "h2" priority low
                exit
        """%(qos_value,qos_value,qos_value,qos_value,qos_value,qos_value,qos_value,qos_value,qos_value,qos_value,qos_value,qos_value,qos_value,qos_value)

        return var_qos


        
