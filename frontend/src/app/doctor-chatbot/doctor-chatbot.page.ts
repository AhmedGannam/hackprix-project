import { Component } from '@angular/core';
import { HttpClient } from '@angular/common/http';

interface ChatMessage {
  sender: 'user' | 'bot';
  text: string;
}

@Component({
  selector: 'app-doctor-chatbot',
  templateUrl: './doctor-chatbot.page.html',
  styleUrls: ['./doctor-chatbot.page.scss'],
  standalone: false
})
export class DoctorChatbotPage {
  messages: ChatMessage[] = [
    { sender: 'bot', text: 'Hello! I am your AI doctor. How can I help you today?' }
  ];
  userInput: string = '';
  loading: boolean = false;

  constructor(private http: HttpClient) { }

  async sendMessage() {
    const question = this.userInput.trim();
    if (!question) return;
    this.messages.push({ sender: 'user', text: question });
    this.userInput = '';
    this.loading = true;
    try {
  const res: any = await this.http.post('http://127.0.0.1:8000/ask', { question }).toPromise();
      this.messages.push({ sender: 'bot', text: res.answer });
    } catch (err) {
      this.messages.push({ sender: 'bot', text: 'Sorry, there was an error. Please try again.' });
    }
    this.loading = false;
  }
}
