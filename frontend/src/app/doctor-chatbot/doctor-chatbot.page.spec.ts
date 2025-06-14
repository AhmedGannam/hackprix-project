import { ComponentFixture, TestBed } from '@angular/core/testing';
import { DoctorChatbotPage } from './doctor-chatbot.page';

describe('DoctorChatbotPage', () => {
  let component: DoctorChatbotPage;
  let fixture: ComponentFixture<DoctorChatbotPage>;

  beforeEach(() => {
    fixture = TestBed.createComponent(DoctorChatbotPage);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
