import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { WorkOrderRadioComponent } from './work-order-radio.component';

describe('WorkOrderRadioComponent', () => {
  let component: WorkOrderRadioComponent;
  let fixture: ComponentFixture<WorkOrderRadioComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ WorkOrderRadioComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(WorkOrderRadioComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
