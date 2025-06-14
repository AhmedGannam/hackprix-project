import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';

import { DoctorChatbotPage } from './doctor-chatbot.page';

const routes: Routes = [
  {
    path: '',
    component: DoctorChatbotPage
  }
];

@NgModule({
  imports: [RouterModule.forChild(routes)],
  exports: [RouterModule],
})
export class DoctorChatbotPageRoutingModule {}
