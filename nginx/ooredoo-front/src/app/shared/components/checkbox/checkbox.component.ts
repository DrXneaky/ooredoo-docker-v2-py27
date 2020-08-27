import { Component, ViewEncapsulation, OnInit, ViewChild, Input, Output, EventEmitter } from '@angular/core';
import { MultiSelectComponent } from '@syncfusion/ej2-angular-dropdowns';
import { CheckBoxComponent } from '@syncfusion/ej2-angular-buttons';


@Component({
  selector: 'nao-checkbox',
  templateUrl: './checkbox.component.html',
  styleUrls: ['./checkbox.component.scss'],
  encapsulation: ViewEncapsulation.None
})
export class CheckboxComponent implements OnInit {

  @ViewChild('checkbox')
  public mulObj: MultiSelectComponent;
  @ViewChild('selectall')
  public checkboxObj: CheckBoxComponent;
  @ViewChild('dropdown')
  public dropdownObj: CheckBoxComponent;
  @ViewChild('select')
  public reorderObj: CheckBoxComponent;
  public mode: string;
  @Input() filterPlaceholder: String = 'Search..';
  //define the data with category
  @Input() data: { [key: string]: Object }[] = [
    { Name: 'Australia', Code: 'AU' },
    { Name: 'Bermuda', Code: 'BM' },
    { Name: 'Canada', Code: 'CA' },
    { Name: 'Cameroon', Code: 'CM' },
    { Name: 'Denmark', Code: 'DK' },
    { Name: 'France', Code: 'FR' },
    { Name: 'Finland', Code: 'FI' },
    { Name: 'Germany', Code: 'DE' },
    { Name: 'Greenland', Code: 'GL' },
    { Name: 'Hong Kong', Code: 'HK' },
    { Name: 'India', Code: 'IN' },
    { Name: 'Italy', Code: 'IT' },
    { Name: 'Japan', Code: 'JP' },
    { Name: 'Mexico', Code: 'MX' },
    { Name: 'Norway', Code: 'NO' },
    { Name: 'Poland', Code: 'PL' },
    { Name: 'Switzerland', Code: 'CH' },
    { Name: 'United Kingdom', Code: 'GB' },
    { Name: 'United States', Code: 'US' }
  ];
  // map the groupBy field with category column
  @Input() checkFields: Object = { text: 'Name', value: 'Code' };
  // set the placeholder to the MultiSelect input
  @Input() checkWaterMark: string = 'Select ..';
  // set the MultiSelect popup height
  @Input() popHeight: String = "150px";
  // set the label
  @Input() label: String;
  //set hte filter placeHolder
  @Input() enableGroupCheckBox: Boolean;
  //onchange event
  @Output() onChangeEvent: EventEmitter<any> = new EventEmitter<any>();

  ngOnInit(): void {
    this.mode = 'CheckBox';
    //this.filterPlaceholder = 'Search countries';
  }
  public onChange(): void {
    // enable or disable the select all in Multiselect based on CheckBox checked state
    this.mulObj.showSelectAll = this.checkboxObj.checked;
  }
  public onChangeDrop(): void {
    // enable or disable the dropdown button in Multiselect based on CheckBox checked state
    this.mulObj.showDropDownIcon = this.dropdownObj.checked;
  }
  public onChangeReorder(): void {
    // enable or disable the list reorder in Multiselect based on CheckBox checked state
    this.mulObj.enableSelectionOrder = this.reorderObj.checked;
  }

  onChangeSelect(event: any) {
    this.onChangeEvent.emit(event.value);
  }
}
