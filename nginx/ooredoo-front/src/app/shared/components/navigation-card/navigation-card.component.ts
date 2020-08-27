import { Component, OnInit, Input } from '@angular/core';
import { NavigationConfig } from './navigation-card-config';


@Component({
  selector: 'ui-navigation-card',
  templateUrl: './navigation-card.component.html',
  styleUrls: ['./navigation-card.component.scss']
})
export class NavigationCardComponent implements OnInit {

  @Input() config: NavigationConfig;

  constructor() { }

  ngOnInit() {
  }

}
