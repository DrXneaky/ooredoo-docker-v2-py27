import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { CollectDashboardComponent } from './collect-dashboard.component';

describe('CollectDashboardComponent', () => {
  let component: CollectDashboardComponent;
  let fixture: ComponentFixture<CollectDashboardComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ CollectDashboardComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(CollectDashboardComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
