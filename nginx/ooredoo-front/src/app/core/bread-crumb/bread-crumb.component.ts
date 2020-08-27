import { Component, OnInit, Input } from '@angular/core';
import { Router, ActivatedRoute, NavigationEnd } from '@angular/router';
import { Title } from '@angular/platform-browser';
import { filter, map, mergeMap } from 'rxjs/operators';

@Component({
  selector: 'ui-bread-crumb',
  templateUrl: './bread-crumb.component.html',
  styleUrls: ['./bread-crumb.component.scss']
})
export class BreadCrumbComponent implements OnInit {

  @Input() layout;
  pageInfo;
  constructor(
    private router: Router,
    private activatedRoute: ActivatedRoute,
    private titleService: Title
  ) {
    // this.router.events.pipe(
    //   filter(event => event instanceof NavigationEnd)
    // ).pipe(map(() => this.activatedRoute)).pipe(
    //   map(route => {
    //     while (route.firstChild) { route = route.firstChild; }
    //     return route;
    //   })).pipe(
    //   filter(route => route.outlet === 'primary')).pipe(
    //   mergeMap(route => route.data))
    //   .subscribe((event) => {
    //     this.titleService.setTitle(event['title']);
    //     this.pageInfo = event;
    //   });
    this.router.events.pipe(
      filter(event => event instanceof NavigationEnd),
      map(() => this.activatedRoute),
      map(route => {
        while (route.firstChild) { route = route.firstChild; }
        return route;
      }),
      filter(route => route.outlet === 'primary'),
      mergeMap(route => route.data))
      .subscribe((event) => {
        this.titleService.setTitle(event['title']);
        this.pageInfo = event;
      });
  }

  ngOnInit() {
  }

}
