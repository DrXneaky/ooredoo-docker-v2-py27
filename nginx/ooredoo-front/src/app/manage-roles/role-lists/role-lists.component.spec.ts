import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { RoleListsComponent } from './role-lists.component';

describe('RoleListsComponent', () => {
  let component: RoleListsComponent;
  let fixture: ComponentFixture<RoleListsComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ RoleListsComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(RoleListsComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
