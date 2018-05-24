import { Component, OnInit } from '@angular/core';
import { first } from 'rxjs/operators';

import { User, Event,BloodType,Storage ,Message, BLOOD_TYPES} from '../_models';
import { UserService, AuthenticationService} from '../_services';
import { EventService } from '../_services/event.service';

// import fade in animation
import * as Typed from "typed.js";

@Component({templateUrl: 'home.component.html',
styleUrls: ['home.component.css']

})
export class HomeComponent implements OnInit {
    currentUser: User;
    users: User[] = [];
    events: Event[] = [];
    storages: Storage[] = [];
    blood: BloodType;
    userId:any;
    messages: Message[] =[];
    message_length = 0;
    active:boolean = false;
    currentMessage:Message;
    respond: string = "";

    constructor(private userService: UserService,private authenticationService: AuthenticationService,private eventService: EventService) {
        //this.currentUser = JSON.parse(localStorage.getItem('currentUser'));
       
    }

    ngOnInit() {
        
        
      

        //this.loadAllUsers();
        
        this.loadUserDetails();

 
        //this.loadMessages();

       
        
        
        
        
    }

    toggle(bool){
        this.active = bool;
        console.log(this.active);
    }

    deleteUser(id: number) {
        this.userService.delete(id).pipe(first()).subscribe(() => { 
            this.loadAllUsers() 
        });
    }

    loadUserDetails() {
        this.userService.getDetails().pipe(first()).subscribe(user => { 
            this.currentUser = user;
            var options = {
            strings: ["Welcome, "+this.currentUser.first_name],
            typeSpeed: 40,
            showCursor: false
          }
          
          var typed = new Typed("#home_text", options);
      
            this.loadMessages();
        });
    }


    private loadAllUsers() {
        this.userService.getAll().pipe(first()).subscribe(users => { 
            this.users = users; 
        });
    }

    private loadMessages() {
        this.eventService.getAllMessages(this.currentUser.user_id).pipe(first()).subscribe(messages => { 
            this.messages = messages; 
            messages.forEach(element => {
                if(element.is_read == 0){
                    this.message_length++;
                }
            });
        });
    }

   


    respondM(){
        
        this.eventService.sendMessage({message_from: this.currentMessage.message_to, message_to: this.currentMessage.message_from, message_body: this.respond, is_read: false}).pipe(first()).subscribe(() =>{
            console.log("sent");
            
        });
        this.markAsRead(this.currentMessage.id);

    }

    setMessage(m){
        this.currentMessage = m;
    }

    markAsRead(id){
        this.eventService.deleteMessage(id).pipe(first()).subscribe(() => { 
            this.messages= this.messages.filter(obj => obj.id !== id);
            this.message_length--;

        });
    }
    

    logout(){
        this.authenticationService.logout().pipe(first()).subscribe(() => {
            console.log("logged out");
        })
    }
}