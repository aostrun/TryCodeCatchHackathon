import { Component, OnInit } from '@angular/core';
import { first } from 'rxjs/operators';

import { User, Event,BloodType,Storage ,Message} from '../_models';
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
    constructor(private userService: UserService,private authenticationService: AuthenticationService,private eventService: EventService) {
        this.currentUser = JSON.parse(localStorage.getItem('currentUser'));
    }

    ngOnInit() {
        
        var options = {
            strings: ["Dobrodošao, ime  i prezime"],
            typeSpeed: 40
          }
          
        var typed = new Typed("#home_text", options);
        
        //this.loadAllUsers();
        //this.loadAllEvents();
        this.loadUserId();
        this.loadAllStorages();
        //this.loadMessages();
    }

    deleteUser(id: number) {
        this.userService.delete(id).pipe(first()).subscribe(() => { 
            this.loadAllUsers() 
        });
    }

    loadUserId() {
        this.userService.getId().pipe(first()).subscribe(id => { 
            this.userId = id;
            this.loadMessages();
        });
    }


    private loadAllUsers() {
        this.userService.getAll().pipe(first()).subscribe(users => { 
            this.users = users; 
        });
    }

    private loadMessages() {
        this.eventService.getAllMessages(this.userId).pipe(first()).subscribe(messages => { 
            this.messages = messages; 
            messages.forEach(element => {
                if(element.is_read == 0){
                    this.message_length++;
                }
            });
        });
    }


    private loadAllEvents() {
        this.eventService.getAll().pipe(first()).subscribe(events => { 
            this.events = events; 
        });
    }

    private loadAllStorages() {
        this.eventService.getAllStorages().pipe(first()).subscribe(storages => { 
            this.storages = storages; 
        });
    }

    getBlood(id){
        this.eventService.getBloodInStorage(id).pipe(first()).subscribe(blood => { 
            this.blood = blood; 
            
        });
    }

    logout(){
        this.authenticationService.logout().pipe(first()).subscribe(() => {
            console.log("logged out");
        })
    }
}