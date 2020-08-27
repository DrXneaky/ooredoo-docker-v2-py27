import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { AuditListCronjobsComponent } from './audit-list-cronjobs.component';

describe('AuditListComponent', () => {
  let component: AuditListCronjobsComponent;
  let fixture: ComponentFixture<AuditListCronjobsComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [AuditListCronjobsComponent]
    })
      .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(AuditListCronjobsComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
