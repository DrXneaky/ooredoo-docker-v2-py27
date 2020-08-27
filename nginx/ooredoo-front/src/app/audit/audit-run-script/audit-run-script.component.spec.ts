import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { AuditRunScriptComponent } from './audit-run-script.component';

describe('AuditRunScriptComponent', () => {
  let component: AuditRunScriptComponent;
  let fixture: ComponentFixture<AuditRunScriptComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ AuditRunScriptComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(AuditRunScriptComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
