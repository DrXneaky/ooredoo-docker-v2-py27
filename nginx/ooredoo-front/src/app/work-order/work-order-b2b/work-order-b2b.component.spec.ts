import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { WorkOrderB2bComponent } from './work-order-b2b.component';

describe('WorkOrderB2bComponent', () => {
  let component: WorkOrderB2bComponent;
  let fixture: ComponentFixture<WorkOrderB2bComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ WorkOrderB2bComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(WorkOrderB2bComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
