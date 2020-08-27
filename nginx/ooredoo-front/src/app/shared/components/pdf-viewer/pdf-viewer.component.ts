import { Component, OnInit, Input } from '@angular/core';
import { $API_URL } from '../../env'

@Component({
  selector: 'nao-pdf-viewer',
  templateUrl: './pdf-viewer.component.html',
  styleUrls: ['./pdf-viewer.component.scss']
})
export class PdfViewerComponent implements OnInit {

  //pdfSrc = "https://vadimdez.github.io/ng2-pdf-viewer/assets/pdf-test.pdf";
  @Input() filename: String = "";
  pdfSrc: String;

  constructor() { }

  ngOnInit() {
    this.pdfSrc = $API_URL + "view-pdf-file/" + this.filename.split('.')[0] + '.pdf';
    //this.pdfSrc = $API_URL + "view-pdf-file/file.pdf";
  }

  //callBackFn(pdf: PDFDocumentProxy)
  callBackFn(pdf) {
    //do anything with pdf
  }


}
