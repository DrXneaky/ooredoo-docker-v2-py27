import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { WorkOrderRadioDetailComponent } from './work-order-radio-detail.component';

describe('WorkOrderRadioDetailComponent', () => {
  let component: WorkOrderRadioDetailComponent;
  let fixture: ComponentFixture<WorkOrderRadioDetailComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ WorkOrderRadioDetailComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(WorkOrderRadioDetailComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
