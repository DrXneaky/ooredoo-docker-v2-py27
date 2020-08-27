import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { DevicesDashboardComponent } from './devices-dashboard.component';

describe('DevicesDashboardComponent', () => {
  let component: DevicesDashboardComponent;
  let fixture: ComponentFixture<DevicesDashboardComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ DevicesDashboardComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(DevicesDashboardComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
