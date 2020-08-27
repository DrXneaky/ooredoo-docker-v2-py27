# -*- coding: utf-8 -*-
from urllib3 import quote
import xlrd
class models:
    def _init_(self,path,CLIENT,listClient,ligne,listClients,mySheet,routerID,test):
        self.path=path
        self.CLIENT=CLIENT
        self.listClient=listClient
        self.ligne=ligne
        self.mySheet=mySheet
        self.listClients=listClients
        self.listClient=listClient
        self.routerID=routerID
        self.test=test


    def _Getclient(self,ClientCode,mySheet):
        num_rows=mySheet.nrows-1
        listClient=mySheet.col_values(1)
        listClient.remove(listClient[0])
        return listClient

    def _My_Sheet(self,path):
        myBook = xlrd.open_workbook(path)
        mySheet=myBook.sheet_by_index(0)
        return mySheet

    def _findClientAttribute(self,index,CLIENT,listClient,mySheet,model):
        dicti =dict()
        ClientAttributes = []

        dicti = {"index":index,
                    "client":str(mySheet.cell_value(index,1)),
                    "Service-id":str(mySheet.cell_value(index,50)),
                    "service":str(mySheet.cell_value(index,20)),
                    "OMIPpba":str(mySheet.cell_value(index,12)),
                    "VPNIPpba":str(mySheet.cell_value(index,34)),
                    "HSIIPpba":str(mySheet.cell_value(index,32)),
                    "port":str(mySheet.cell_value(index,15)),
                    "OMvlan":str(mySheet.cell_value(index,18)),
                    "HSIvlan":str(mySheet.cell_value(index,47)),
                    "VPNvlan":str(mySheet.cell_value(index,49)),
                    "VOIPvlan":str(mySheet.cell_value(index,48)),
                    "Protocol_type":str(quote(mySheet.cell_value(index,42).encode("utf-8"))),
                    "Authentication_Key":mySheet.cell_value(index,39),
                    "Interface_Name":str(model._find_Interface_Name(mySheet,index)),
                    "QOS":mySheet.cell_value(index,19),
                    "VpnDescription":str(mySheet.cell_value(index,2).encode('utf-8')),
                    "publicIP":str(mySheet.cell_value(index,22)),
                    "IPCpeHSIAdress":str(mySheet.cell_value(index,28)),
                    "VOIPIPpba":str(mySheet.cell_value(index,33)),
                    "loopbackOM":str(mySheet.cell_value(index,13)),
                    "IPOMCpeAdress":str(mySheet.cell_value(index,11)),
                    "LoopbackVOIP":str(mySheet.cell_value(index,31)),
                    "routes":mySheet.cell_value(index,9),
                    "IPVPNCpeAdress":str(mySheet.cell_value(index,30))
                    }
        ClientAttributes.append(dicti)
        return ClientAttributes

    def _findClient(self,CLIENT,listClient):
        listClients=[]
        for index,client in enumerate(listClient):
                if CLIENT==client:
                        mon_tuple =index+1,client.encode("utf-8")
                        listClients.append(mon_tuple)
        return listClients


    def _findService(self,listClients,mySheet):
        service=[]
        for x in listClients:
            service.append(str(mySheet.cell_value(x[0],20)))
        return service

    def _findRouter(self,ligne,listClients,mySheet):
        ligne=listClients[0][0]
        PE=str(mySheet.cell_value(ligne,14))
        PE=PE.split("PE")[1]
        return str(PE)

    def _ExtraireRD(self,mySheet,routerID):
        num_rows=mySheet.nrows-1
        add=[]
        curr_row=1
        while curr_row < num_rows:
            cell_value=int(mySheet.cell_value(curr_row,0))
            if str(cell_value) == routerID:
                add.append(mySheet.cell_value(curr_row,1))
            curr_row+=1
        return(add)

    def _find_Interface_Name(self,mySheet,index):
        z=(mySheet.cell(index,0)).value
        z=z.split(" ")
        VpnDescription=z[0]
        for x in z:
            s="_"
            if ("SITE" in x) or ("site" in x) or ("Site" in x) :
                z.remove(x)
            y=s.join(z)
        y=y.encode("ascii", "ignore")
        y=str(y)
        return y
