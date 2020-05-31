import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { MainAppLayoutComponent } from './main-app-layout.component';

describe('MainAppLayoutComponent', () => {
  let component: MainAppLayoutComponent;
  let fixture: ComponentFixture<MainAppLayoutComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ MainAppLayoutComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(MainAppLayoutComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
