import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { WorkOrderDashboardComponent } from './work-order-dashboard.component';

describe('WorkOrderDashboardComponent', () => {
  let component: WorkOrderDashboardComponent;
  let fixture: ComponentFixture<WorkOrderDashboardComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ WorkOrderDashboardComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(WorkOrderDashboardComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
