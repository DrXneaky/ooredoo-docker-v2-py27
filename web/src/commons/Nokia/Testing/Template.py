# -*- coding: utf-8 -*-
import os
import sys
from netaddr import *
from ..Connection import Nokia_Connection
from ..Models.Models import models
from src.commons.Nokia.Service.Check import Check
from src.commons.Nokia.Service.InternetService import HSIServices
from src.commons.Nokia.Service.OMCorporateService import OMServices
from src.commons.Nokia.Service.VPNService import VPNServices
from src.commons.Nokia.Service.QOS import qos
from src.commons.Nokia.Service.Trunk_Sip import TrunkSipServices
from src.commons.Nokia.Service.Policy import policy

model = models()
Mysheet = model._My_Sheet('C:/Users/HP/Desktop/doc ghassen/pfe_2020/ooredoo-back/ressources/formulaire.xls')
CLIENT = str(sys.argv[1])
Service_Type = str(sys.argv[2])
Device_type = str(sys.argv[3])
# CLIENT="SFX_8981"

Getclients = model._Getclient(CLIENT, Mysheet)

clients = model._findClient(CLIENT, Getclients)

ServicesdeClient = model._findService(clients, Mysheet)

Policy = policy()

indexs = []
for elem in clients:
    indexs.append(elem[0])

VPNServiceInstance = VPNServices()
VOIPServiceInstance = TrunkSipServices()
HSIServiceInstance = HSIServices()
OMServiceInstance = OMServices()
x = Nokia_Connection.Connection("192.168.161.9")
net_connect = x._NokiaConnection()
check = Check()
QOS = qos()
rd = "002"
subnets = ["10.123.10.0/30", "10.124.10.0/30"]
nexthop = "10.123.10.2/30"
Protocol_type = "OSPF"


def _Run_ServiceVPN(VPNServiceInstance, check, Protocol_type, net_connect, Serviceid):
    if Device_type == "Nokia":
        if Protocol_type == "OSPF":
            Intero = IPNetwork(IPpbaVPN).cidr
            Filter_VPN = Policy._filter_VPN(Intero)
            checkInstance = check._CheckServiceExistance(Serviceid, net_connect)
            if (checkInstance == "TRUE"):
                VPNService = VPNServiceInstance._OSPF_Old_VPN_Service(Serviceid, interface_name, interface_name,
                                                                      IPpbaVPN, port, vlanVPN, qos_ingress, qos_egress,
                                                                      interface_name, Authentication_Key)
            else:

                VPNService = VPNServiceInstance._OSPF_New_VPN_Service(Serviceid, interface_name, rd, interface_name,
                                                                      interface_name, IPpbaVPN, port, vlanVPN,
                                                                      qos_ingress, qos_egress, interface_name,
                                                                      Authentication_Key, VpnDescription)

        else:
            checkInstance = check._CheckServiceExistance(Serviceid, net_connect)
            if (checkInstance == "TRUE"):
                VPNService = VPNServiceInstance._STATIC_Old_VPN_Service(Serviceid, interface_name, interface_name,
                                                                        IPpbaVPN, port, vlanVPN, Authentication_Key,
                                                                        routes, IPVPNCpeAdress)
            else:
                VPNService = VPNServiceInstance._STATIC_New_VPN_Service(Serviceid, interface_name, rd, interface_name,
                                                                        interface_name, port, vlanVPN,
                                                                        Authentication_Key, routes, IPVPNCpeAdress)

        print(VPNService)

    elif Device_type == "Cisco":
        if Protocol_type == "OSPF":
            Intero = IPNetwork(IPpbaVPN).cidr
            Filter_VPN = Policy._filter_VPN(Intero)
            checkInstance = check._CheckVRFExistance(Serviceid, net_connect)
            if (checkInstance == "TRUE"):
                VPNService = VPNServiceInstance._OSPF_Old_VPN_Service(Serviceid, interface_name, interface_name,
                                                                      IPpbaVPN, port, vlanVPN, qos_ingress, qos_egress,
                                                                      interface_name, Authentication_Key)
            # else:
            #     Serviceid, = Create_New_VRF()
            #     VPNService = VPNServiceInstance._OSPF_New_VPN_Service(Serviceid, interface_name, rd, interface_name,
            #                                                           interface_name, IPpbaVPN, port, vlanVPN,
            #                                                           qos_ingress, qos_egress, interface_name,
            #                                                           Authentication_Key, VpnDescription)

        else:
            checkInstance = check._CheckServiceExistance(Serviceid, net_connect)
            if (checkInstance == "TRUE"):
                VPNService = VPNServiceInstance._STATIC_Old_VPN_Service(Serviceid, interface_name, interface_name,
                                                                        IPpbaVPN, port, vlanVPN, Authentication_Key,
                                                                        routes, IPVPNCpeAdress)
            else:
                VPNService = VPNServiceInstance._STATIC_New_VPN_Service(Serviceid, interface_name, rd, interface_name,
                                                                        interface_name, port, vlanVPN,
                                                                        Authentication_Key, routes, IPVPNCpeAdress)

        print(VPNService)

    return VPNService


def RunServiceTrunkSip(VOIPServiceInstance, check, Protocol_type, net_connect):
    if Device_type == "Nokia":
        if Protocol_type == "OSPF":
            checkResponse = check._CheckServiceExistance("5061", net_connect)
            Intero = IPNetwork(VOIPIPpba).cidr
            Filter_VOIP = Policy._filter_VOIP(Intero)
            From_Loopback_VOIP_OSPF = Policy._from_Loopback_VOIP_OSPF_policy(check, net_connect, LoopbackVOIP)
            if checkResponse == "TRUE":
                VOIPService = VOIPServiceInstance._OSPF_Old_OSPF_VOIP_Service(interface_name, interface_name, VOIPIPpba,
                                                                              port, VOIPvlan)
            else:
                VOIPService = VOIPServiceInstance._OSPF_New_OSPF_VOIP_Service(rd, interface_name, interface_name,
                                                                              VOIPIPpba, port, VOIPvlan, interface_name,
                                                                              Authentication_Key)
        else:
            Filter_VOIP = ""
            From_Loopback_VOIP_OSPF = ""
            checkResponse = check._CheckServiceExistance("5061", net_connect)
            if checkResponse == "TRUE":
                VOIPService = VOIPServiceInstance._OSPF_old_Static_VOIP_Service(interface_name, interface_name,
                                                                                VOIPIPpba, port, VOIPvlan)
            else:
                VOIPService = VOIPServiceInstance._OSPF_New_Static_VOIP_Service(rd, interface_name, VOIPIPpba, port,
                                                                                VOIPvlan)
        VOIPService = Filter_VOIP + "\n" + From_Loopback_VOIP_OSPF + "\n" + VOIPService
        print(VOIPService)
    elif Device_type == "Cisco":
        if Protocol_type == "OSPF":
            print("hello")
    return VOIPService


def RunServiceHSI(HSIServiceInstance, check, Protocol_type, net_connect):
    if Device_type == "Nokia":
        if Protocol_type == "OSPF":
            HSIService = HSIServiceInstance._OSPF_HSI_Service(interface_name, interface_name, HSIIPpba, port, HSIvlan,
                                                              qos_ingress, qos_egress, interface_name,
                                                              Authentication_Key)
            public_HSI = Policy._filter_public_HSI(check, publicIP, net_connect)
            checkHSIloopback = check._Check_HSI_loopback(net_connect)
            if checkHSIloopback == "TRUE":
                Hsiservice = ""
            else:
                Hsiservice = HSIServiceInstance._OSPF_Configure_HSI_loopback("10.222.22.3")
            HSIService = HSIService + "\n" + Hsiservice

        else:
            HSIService = HSIServiceInstance._Static_HSI_Service(interface_name, interface_name, HSIIPpba, port, HSIvlan,
                                                                qos_ingress, qos_egress, publicIP, IPHSICpeAdress)
        print(HSIService)
    elif Device_type == "Cisco":
        print("test_is_ok")

    return HSIService


def RunServiceOM(OMServiceInstance, check, Protocol_type, Policy, net_connect):
    if Device_type == "Nokia":
        if Protocol_type == "OSPF":
            Intero = IPNetwork(OMIPpba).cidr
            Policy_output = Policy._filter_OM(Intero)
            LoopbackOM_policy = Policy._from_LoopbackOM_policy(check, net_connect, loopbackOM)
            LoopbackOM_policy_ospf = Policy._from_LoopbackOM_OSPF_policy(check, net_connect)
            checkInstance = check._CheckServiceExistance(Serviceid, net_connect)
            if checkInstance == "TRUE":
                OMService = OMServiceInstance.Old_OSPF_OM_Service(interface_name, interface_name, OMIPpba, port, OMvlan,
                                                                  interface_name, Authentication_Key)
            else:
                OMService = OMServiceInstance.New_OSPF_OM_Service(rd, interface_name, interface_name, OMIPpba, port,
                                                                  OMvlan, interface_name, Authentication_Key)
        else:
            OMService = OMServiceInstance._Static_OM_Service(interface_name, interface_name, OMIPpba, port, OMvlan,
                                                             loopbackOM, IPOMCpeAdress)
        OMService_output = Policy_output + "\n" + LoopbackOM_policy + "\n" + LoopbackOM_policy_ospf + "\n" + OMService
        print(OMService_output)
        return OMService_output
    elif Device_type == "Cisco":
        print("test_is_ok")


for index in indexs:
    clientAttribute = model._findClientAttribute(index, CLIENT, clients, Mysheet, model)
    for elem1 in clientAttribute:
        service = elem1["service"]
        client = elem1["client"]
        Serviceid = elem1["Service-id"]
        loopbackOM = elem1["loopbackOM"]
        OMIPpba = elem1["OMIPpba"]
        IPHSICpeAdress = elem1["IPCpeHSIAdress"]
        IPOMCpeAdress = elem1["IPOMCpeAdress"]
        IPVPNCpeAdress = elem1["IPVPNCpeAdress"]
        LoopbackVOIP = elem1["LoopbackVOIP"]
        IPpbaVPN = elem1["VPNIPpba"]
        HSIIPpba = elem1["HSIIPpba"]
        VOIPIPpba = elem1["VOIPIPpba"]
        port = elem1["port"]
        OMvlan = elem1["OMvlan"]
        HSIvlan = elem1["HSIvlan"]
        vlanVPN = elem1["VPNvlan"]
        VOIPvlan = elem1["VOIPvlan"]
        Protocol_type = elem1["Protocol_type"]
        Authentication_Key = elem1["Authentication_Key"]
        interface_name = elem1["Interface_Name"]
        VpnDescription = elem1["VpnDescription"]
        publicIP = elem1["publicIP"]
        BAND = str(elem1["QOS"])
        routes = elem1["routes"]
        Bandwith = BAND.split(".")
        BANDWITH = Bandwith[0]
        BANDWITH_Value = QOS._Get_Bandwith(check, QOS, BANDWITH)
        qos_ingress = BANDWITH_Value[0]
        qos_egress = BANDWITH_Value[1]
        if Service_Type == "Normal":
            if service == "Trunk SIP":
                RunServiceTrunkSip(VOIPServiceInstance, check, Protocol_type, net_connect)
            if service == "VPN MPLS":
                _Run_ServiceVPN(VPNServiceInstance, check, Protocol_type, net_connect, Serviceid)
            if service == "Internet":
                RunServiceHSI(HSIServiceInstance, check, Protocol_type, net_connect)
            if service == "OM_Corporate":
                Protocol_type = "OSPF"
                RunServiceOM(OMServiceInstance, check, Protocol_type, Policy, net_connect)
        elif Service_Type == "VPLS_MH":
