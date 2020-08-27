import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { WorkOrderAdvancedComponent } from './work-order-advanced.component';

describe('WorkOrderAdvancedComponent', () => {
  let component: WorkOrderAdvancedComponent;
  let fixture: ComponentFixture<WorkOrderAdvancedComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ WorkOrderAdvancedComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(WorkOrderAdvancedComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
