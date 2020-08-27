import { Component, OnInit, Inject } from '@angular/core';
import { MAT_DIALOG_DATA, MatDialogRef } from "@angular/material";

@Component({
  selector: 'nao-dialog-body',
  templateUrl: './dialog-body.component.html',
  styleUrls: ['./dialog-body.component.scss']
})
export class DialogBodyComponent implements OnInit {

  report: String;

  constructor(
    private dialogRef: MatDialogRef<DialogBodyComponent>,
    @Inject(MAT_DIALOG_DATA) data) {

    this.report = data.report;
  }

  ngOnInit() {
    console.log(this.report);
  }

  close() {
    this.dialogRef.close();
  }

}
