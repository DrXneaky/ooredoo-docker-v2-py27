import xlrd
import sys
#sys.path.insert(0, 'C:/Users/HPDesktop/doc ghassen/pfe_2020/ooredoo-back/src/commons/utils/')

#from excel_manager_config import timos_excel_file
from src.commons.utils.excel_manager_config import timos_excel_file

print(timos_excel_file)
def create_interface_name(sheet_timos ,index):
    site_name = (sheet_timos.cell(index,0)).value
    site_name =site_name.split(" ")
    for element in site_name :
        s="_"
        if ("SITE" in element) or ("site" in element) or ("Site" in element):
            site_name.remove(element)
        interface_name= s.join(site_name)

    # interface_name = str(interface_name.encode("ascii", "ignore"))
    interface_name = str(interface_name)
    return interface_name

def fetch_client_services(target_client):
    client_attributes = []
    services = []
    formulaire_timos = xlrd.open_workbook(timos_excel_file)
    sheet_timos = formulaire_timos.sheet_by_index(0)
    all_clients = sheet_timos.col_values(1)
    all_clients.remove(all_clients[0])
    #listClients = [(index + 1, client_code.encode("utf-8")) for index, client_code in enumerate(all_clients) if target_client == client_code]
    try:
        for index, client_code in enumerate(all_clients):
            if target_client == client_code:
                index = index +1
                dicti = {"index": index,
                        "hostname" : sheet_timos.cell_value(index, 14).encode('utf-8'),
                        "client": sheet_timos.cell_value(index, 1).encode('utf-8'),
                        "serviceid": sheet_timos.cell_value(index, 50).encode('utf-8'),
                        "service": sheet_timos.cell_value(index, 20).encode('utf-8'),
                        "om_ip_pba": sheet_timos.cell_value(index, 12).encode('utf-8'),
                        "vpn_ip_pba": sheet_timos.cell_value(index, 34).encode('utf-8'),
                        "hsi_ip_pba": sheet_timos.cell_value(index, 32).encode('utf-8'),
                        "port": sheet_timos.cell_value(index, 15).encode('utf-8').lower(),
                        "om_vlan": sheet_timos.cell_value(index, 18).encode('utf-8'),
                        "hsi_vlan": sheet_timos.cell_value(index, 47).encode('utf-8'),
                        "vpn_vlan": sheet_timos.cell_value(index, 49).encode('utf-8'),
                        "voip_vlan": sheet_timos.cell_value(index, 48).encode('utf-8'),
                        "protocol_type": sheet_timos.cell_value(index, 42).encode('utf-8'),
                        "authentication_key": sheet_timos.cell_value(index, 39).encode('utf-8'),
                        "interface_name": create_interface_name(sheet_timos, index).encode('utf-8'),
                        "qos": sheet_timos.cell_value(index, 19),
                        "description_vpn": sheet_timos.cell_value(index, 2).encode('utf-8'),
                        "public_ip": sheet_timos.cell_value(index, 22).encode('utf-8').split(";"),
                        #"public_ip": str(sheet_timos.cell_value(index, 22)).split(";"),
                        "ip_hsi_cpe": sheet_timos.cell_value(index, 28).encode('utf-8'),
                        "voip_ip_pba": sheet_timos.cell_value(index, 33).encode('utf-8'),
                        "loopback_om": sheet_timos.cell_value(index, 13).encode('utf-8'),
                        "om_ip_cpe": sheet_timos.cell_value(index, 11).encode('utf-8'),
                        "loopback_voip": sheet_timos.cell_value(index, 31).encode('utf-8'),
                        "ip_vpn_cpe": sheet_timos.cell_value(index, 30).encode('utf-8'),
                        "routes": sheet_timos.cell_value(index, 9).encode('utf-8')
                        }
                if dicti["qos"]:
                    pass
                else:
                    dicti["qos"] = 10
                if dicti["service"] == "OM_Corporate":
                    dicti["serviceid"] = "5101"
                if dicti["service"] =="Internet" :
                    dicti["serviceid"] = "9500"
                if dicti["service"] == "Trunk SIP":
                    dicti["serviceid"] = "5061"
                json_qos = {"vrf_id": dicti["serviceid"], "vrf_name":dicti["description_vpn"] ,"description":dicti["description_vpn"], "qos":dicti["qos"]}
                # routes creer par seif: check with him
                services.append(json_qos)
                client_attributes.append(dicti)
    except Exception:
        for index, client_code in enumerate(all_clients):
            if target_client == client_code:
                index = index +1
                dicti = {"index": index,
                        "hostname" : str(sheet_timos.cell_value(index, 14)),
                        "client": str(sheet_timos.cell_value(index, 1)),
                        "serviceid": str(sheet_timos.cell_value(index, 50)),
                        "service": str(sheet_timos.cell_value(index, 20)),
                        "om_ip_pba": str(sheet_timos.cell_value(index, 12)),
                        "vpn_ip_pba": str(sheet_timos.cell_value(index, 34)),
                        "hsi_ip_pba": str(sheet_timos.cell_value(index, 32)),
                        "port": str(sheet_timos.cell_value(index, 15)).lower(),
                        "om_vlan": str(sheet_timos.cell_value(index, 18)),
                        "hsi_vlan": str(sheet_timos.cell_value(index, 47)),
                        "vpn_vlan": str(sheet_timos.cell_value(index, 49)),
                        "voip_vlan": str(sheet_timos.cell_value(index, 48)),
                        "protocol_type": str(sheet_timos.cell_value(index, 42)),
                        "authentication_key": str(sheet_timos.cell_value(index, 39)),
                        "interface_name": str(create_interface_name(sheet_timos, index)),
                        "qos": sheet_timos.cell_value(index, 19),
                        "description_vpn": str(sheet_timos.cell_value(index, 2)),
                        "public_ip": str(sheet_timos.cell_value(index, 22)).split(";"),
                        #"public_ip": str(sheet_timos.cell_value(index, 22)).split(";"),
                        "ip_hsi_cpe": str(sheet_timos.cell_value(index, 28)),
                        "voip_ip_pba": str(sheet_timos.cell_value(index, 33)),
                        "loopback_om": str(sheet_timos.cell_value(index, 13)),
                        "om_ip_cpe": str(sheet_timos.cell_value(index, 11)),
                        "loopback_voip": str(sheet_timos.cell_value(index, 31)),
                        "ip_vpn_cpe": str(sheet_timos.cell_value(index, 30)),
                        "routes": str(sheet_timos.cell_value(index, 9))
                        }
                if dicti["qos"]:
                    pass
                else:
                    dicti["qos"] = 10
                if dicti["service"] == "OM_Corporate":
                    dicti["serviceid"] = "5101"
                if dicti["service"] =="Internet" :
                    dicti["serviceid"] = "9500"
                if dicti["service"] == "Trunk SIP":
                    dicti["serviceid"] = "5061"
                json_qos = {"vrf_id": dicti["serviceid"], "vrf_name":dicti["description_vpn"] ,"description":dicti["description_vpn"], "qos":dicti["qos"]}
                # routes creer par seif: check with him
                services.append(json_qos)
                client_attributes.append(dicti)
    return client_attributes, services

#
