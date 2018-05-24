import { Component, OnInit } from '@angular/core';
import { first } from 'rxjs/operators';

import { User, Event,BloodType,Storage } from '../_models';
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
    }

    deleteUser(id: number) {
        this.userService.delete(id).pipe(first()).subscribe(() => { 
            this.loadAllUsers() 
        });
    }

    loadUserId() {
        this.userService.getId().pipe(first()).subscribe(id => { 
            this.userId = id;
        });
    }


    private loadAllUsers() {
        this.userService.getAll().pipe(first()).subscribe(users => { 
            this.users = users; 
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

    getBlood(){
        this.eventService.getBloodInStorage(1).pipe(first()).subscribe(blood => { 
            this.blood = blood; 
            console.log(this.blood);
        });
    }

    logout(){
        this.authenticationService.logout().pipe(first()).subscribe(() => {
            console.log("logged out");
        })
    }
}