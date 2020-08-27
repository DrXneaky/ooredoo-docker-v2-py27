import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { WorkOrderRadioListComponent } from './work-order-radio-list.component';

describe('WorkOrderRadioListComponent', () => {
  let component: WorkOrderRadioListComponent;
  let fixture: ComponentFixture<WorkOrderRadioListComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ WorkOrderRadioListComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(WorkOrderRadioListComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
