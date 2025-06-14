import { NgModule } from '@angular/core';
import { PreloadAllModules, RouterModule, Routes } from '@angular/router';

const routes: Routes = [
  {
    path: 'home',
    loadChildren: () => import('./home/home.module').then( m => m.HomePageModule)
  },
  {
    path: 'doctor-chatbot',
    loadChildren: () => import('./doctor-chatbot/doctor-chatbot.module').then( m => m.DoctorChatbotPageModule)
  },
  {
    path: '',
    redirectTo: 'home',
    pathMatch: 'full'
  },
  {
    path: 'doctor-chatbot',
    loadChildren: () => import('./doctor-chatbot/doctor-chatbot.module').then( m => m.DoctorChatbotPageModule)
  },
];

@NgModule({
  imports: [
    RouterModule.forRoot(routes, { preloadingStrategy: PreloadAllModules })
  ],
  exports: [RouterModule]
})
export class AppRoutingModule { }
