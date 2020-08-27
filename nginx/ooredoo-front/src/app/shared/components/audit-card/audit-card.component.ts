import { Component, OnInit, Input } from "@angular/core";
import { AuditNavConfig } from "./audit-card-config";
import { AuditNestedTreeElements } from "./audit-card-config";
import { MatExpansionModule } from '@angular/material/expansion';
import { MatTreeModule } from '@angular/material/tree';
import { NestedTreeControl } from '@angular/cdk/tree';
import { MatTreeNestedDataSource } from '@angular/material/tree';
import { nodeChildrenAsMap } from '@angular/router/src/utils/tree';


@Component({
  selector: "ui-audit-card",
  templateUrl: "./audit-card.component.html",
  styleUrls: ["./audit-card.component.scss"],
})


export class AuditCardComponent implements OnInit {
  @Input() config: AuditNestedTreeElements;
  //@Input() node: AuditNestedTreeElements;

  treeControl = new NestedTreeControl<AuditNestedTreeElements>(node => node.children);
  dataSource = new MatTreeNestedDataSource<AuditNestedTreeElements>();

  constructor() {
  }

  hasChild = (_: number, node: AuditNestedTreeElements) => !!node.children && node.children.length > 0;

  ngOnInit() { }


}
