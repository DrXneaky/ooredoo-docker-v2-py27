import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { AuditListScriptsComponent } from './audit-list-scripts.component';

describe('AuditListScriptsComponent', () => {
  let component: AuditListScriptsComponent;
  let fixture: ComponentFixture<AuditListScriptsComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ AuditListScriptsComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(AuditListScriptsComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
