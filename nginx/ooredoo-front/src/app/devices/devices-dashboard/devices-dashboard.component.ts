import { Component, OnInit, ViewChild, ElementRef } from '@angular/core';
import { FormGroup, FormBuilder, FormControl, Validators } from '@angular/forms';
import { Device, Vendor } from 'src/app/work-order/work-order-list/work-order-list-config';
import { DeviceService } from 'src/app/shared/services/device.service';
import { ToastrService } from 'ngx-toastr';
import { ValidateRequiredSelect } from 'src/app/work-order/work-order-b2b/work-order-b2b-config';
import { SheetService } from 'src/app/shared/services/sheet.service';
import { NgbModal, ModalDismissReasons } from "@ng-bootstrap/ng-bootstrap";
import * as XLSX from 'xlsx';


type AOA = any[][];
@Component({
  selector: 'nao-devices-dashboard',
  templateUrl: './devices-dashboard.component.html',
  styleUrls: ['./devices-dashboard.component.scss']
})
export class DevicesDashboardComponent implements OnInit {
  @ViewChild("content") content: ElementRef;

  deviceFormGroup: FormGroup;
  devices: Device[] = [];
  devicses: Device[] = [];
  pageNumber = 1;
  pages = 0;
  allDevice: Device[] = [];
  modalHeader: String = "";
  modalBody: String = "";
  constructor(private formBuilder: FormBuilder,
    private DeviceService: DeviceService,
    private toastr: ToastrService,
    private modalService: NgbModal,
    private sheetService: SheetService) { }

  ngOnInit() {
    this.getDevices(this.pageNumber);
    this.initFormGroup();
  }
  onSubmit(formGroup: FormGroup) {
    this.DeviceService.generateDevice(this.createDevice(formGroup)).subscribe(
      (data: Device) => {
        console.log(data);
        if (data[1] === 200) {
          this.toastr.success(data[0]);
        }
        else {
          this.toastr.error(data[0]);
        }
        this.getDevices(this.pageNumber);
        formGroup.reset({
          hostname: '',
          ipSystem: '',
          rd: ''
        });
      },
      (error: any) => {
        this.toastr.error('The creation of the device is failed');
      }
    );
  }
  initFormGroup() {
    this.deviceFormGroup = this.formBuilder.group(
      {
        hostname: new FormControl('', [Validators.required, Validators.pattern('^[0-9]{4}\_*[A,B]*')]),
        ipSystem: new FormControl('', [Validators.required]),
        rd: new FormControl('', [Validators.required, Validators.pattern('^[0-9]{3}')]),
        vendor: new FormControl(0, Validators.compose([ValidateRequiredSelect]))
      }
    );
  }


  createDevice(formGroup: FormGroup): Device {
    const hostname = formGroup.get('hostname').value;
    const ipSystem = formGroup.get('ipSystem').value;
    const rd = formGroup.get('rd').value;
    const vendor = formGroup.get('vendor').value;
    const device = new Device();
    device.hostname = hostname;
    device.ipSystem = ipSystem;
    device.rd = rd;
    if (vendor === '2') {
      device.vendor = Vendor.CISCO;
    } else if (vendor === '3') {
      device.vendor = Vendor.HUAWEI;
    } else if (vendor === '1') {
      device.vendor = Vendor.NOKIA;
    } else if (vendor === '4') {
      device.vendor = Vendor.SIAE;
    } else {
      device.vendor = null;
    }
    return device;
  }

  getDevices(pageNumber: number) {
    this.DeviceService.getDevices(pageNumber, 7).subscribe((page: any) => {
      this.devices = page.items.data;
      this.pages = page.pages;
    });
  }

  onPageChange(page: number) {
    this.pageNumber = page;
    this.getDevices(this.pageNumber);
  }

  onActionClick(event: any) {
    switch (event.action) {
      case 'EDIT':
        this.modalHeader = "EDIT";
        this.modalBody = "Are you sure you want to Edit this device?";
        this.open(event.device);
        break;
      case 'DELETE':
        this.modalHeader = "DELETE";
        this.modalBody = "Are you sure you want to DELETE this device?";
        this.open(event.device);
        break;
    }
    console.log("problem solved");
  }

  open(device: Device) {
    this.modalService.open(this.content, {
      ariaLabelledBy: "modal-basic-title",
      size: "lg",
      centered: true,
    }).result.then((result) => {
      switch (result) {
        case 'CANCEL':
          break;
        case 'DELETE':
          console.log('deleting');
          this.deleteDevice(device);
          break;
        case 'EDIT':
          this.editDevice(device);
          console.log('editing');
      }
    });
  }

  deleteDevice(device) {
    this.DeviceService.deleteDevice(device).subscribe(
      (result: any) => {
        console.log(result);
        if (result.status == 'done') {
          this.toastr.success('Device ' + result.device + ' was deleted successfully');
        } else if (result.status == 'integrityError') {
          this.toastr.error('Device ' + result.device + ' is used in audit module, you cannot delete it');
        }
      }, error => {
        this.toastr.error('An error occurred while deleting the device');
      }
    );
  }

  editDevice(device) {
    this.DeviceService.editDevice(device).subscribe(
      (result: any) => {
        if (result.status = 'done') {
          this.toastr.success('Device was edited successfully');
        } else {
          this.toastr.error('An error occurred while editing the device');
        }
      }, error => {
        this.toastr.error('An error occurred while editing the device');
      }
    );
  }

  getallDevices(): Device[] {
    this.DeviceService.getAllDevices().subscribe(data => {
      this.devicses = data;
    });
    return this.devicses;
  }


  exportAsXLSX(): void {
    this.sheetService.exportAsExcelFile(this.getallDevices(), 'devices');
  }



  onFileChange(evt: any) {
    var data: any;
    /* wire up file reader */
    const target: DataTransfer = <DataTransfer>(evt.target);
    if (target.files.length !== 1) throw new Error('Cannot use multiple files');
    const reader: FileReader = new FileReader();
    reader.onload = (e: any) => {
      /* read workbook */
      const bstr: string = e.target.result;
      const wb: XLSX.WorkBook = XLSX.read(bstr, { type: 'binary' });

      /* grab first sheet */
      const wsname: string = wb.SheetNames[0];
      const ws: XLSX.WorkSheet = wb.Sheets[wsname];


      /* save data */
      data = <any>(XLSX.utils.sheet_to_json(ws, { header: 1 }));
      console.log(data);
      for (let entry of data) {
        var d = new Device()
        if (entry[0] && entry[1] && entry[2]) {
          d.hostname = entry[0]
          d.ipSystem = entry[1]
          d.rd = entry[2]
          d.vendor = entry[3]
          this.allDevice.push(d)
        }
      }
      if (this.allDevice.length === 1) {
        this.toastr.info('The excel file is empty please check your parameters.');
      }
      else {
        this.DeviceService.uploadDevices(this.allDevice).subscribe(
          (data: any) => {
            if (data[1] === 199) {
              this.toastr.info(data[0]);
            }
            else {
              this.toastr.success(data[0]);
            }
            this.getDevices(this.pageNumber);

          },
          (error: any) => {
            this.toastr.error('The creation of the device is failed');
          }
        );
      }

    };
    reader.readAsBinaryString(target.files[0]);
  }





}
