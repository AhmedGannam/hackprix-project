import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';

import { IonicModule } from '@ionic/angular';

import { DoctorChatbotPageRoutingModule } from './doctor-chatbot-routing.module';

import { DoctorChatbotPage } from './doctor-chatbot.page';

@NgModule({
  imports: [
    CommonModule,
    FormsModule,
    IonicModule,
    DoctorChatbotPageRoutingModule
  ],
  declarations: [DoctorChatbotPage]
})
export class DoctorChatbotPageModule {}
