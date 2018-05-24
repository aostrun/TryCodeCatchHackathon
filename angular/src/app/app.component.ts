import { Component,OnInit } from '@angular/core';
import { fadeAnimation } from './_animations/fade-in.animation';
import { Router} from '@angular/router';
import { HomeComponent} from './home/home.component';
import {
    transition,
    trigger,
    query,
    style,
    animate,
    group,
    animateChild,sequence
  } from '@angular/animations';

@Component({
    selector: 'app',
    templateUrl: 'app.component.html',
    styleUrls: ['app.component.css'],
    animations: [fadeAnimation] // register the animation
})

export class AppComponent{
    

    


    
 }