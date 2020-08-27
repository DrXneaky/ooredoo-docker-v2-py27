import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { AuditAddCronjobComponent } from './audit-add-cronjob.component';

describe('AuditAddCronjobComponent', () => {
  let component: AuditAddCronjobComponent;
  let fixture: ComponentFixture<AuditAddCronjobComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ AuditAddCronjobComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(AuditAddCronjobComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
