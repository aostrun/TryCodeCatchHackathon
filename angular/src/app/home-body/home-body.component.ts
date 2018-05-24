import { Component, OnInit,Input} from '@angular/core';
import { User, Event,BloodType,Storage ,Message, BLOOD_TYPES} from '../_models';
import { EventService } from '../_services/event.service';
import { first } from 'rxjs/operators';
import * as Typed from "typed.js";

declare var google:any;

@Component({
  selector: 'app-home-body',
  templateUrl: './home-body.component.html',
  styleUrls: ['./home-body.component.css']
})
export class HomeBodyComponent implements OnInit {
  @Input() currentUser: User;
  users: User[] = [];
  events: Event[] = [];
  blood: BloodType;
  @Input() storages: Storage[] = [];


  constructor(private eventService: EventService) { }

  ngOnInit() {

    var options = {
      strings: ["Welcome ,"+this.currentUser.first_name],
      typeSpeed: 40
    }
    
    var typed = new Typed("#home_text", options);
    
  }

  init(){
    google.charts.load('current', {'packages':['corechart']});
    google.charts.setOnLoadCallback(drawChart);
    var self = this;
    // Draw the chart and set the chart values
    function drawChart() {
      var data = google.visualization.arrayToDataTable([
      ['Blood type','How much in warehouse'],
      ["0-", self.blood["0-"]],
      ['0+', self.blood["0+"]],
      ['A-', self.blood["A-"]],
      ['A+', self.blood["A+"]],
      ['B-', self.blood["B-"]],
      ['B+', self.blood["B+"]],
      ['AB-', self.blood["AB-"]],
      ['AB+', self.blood["AB+"]]
    ]);
    
      // Optional; add a title and set the width and height of the chart
      var options = {'title':'Blood storage', 'width':300, 'height':300};
    
      // Display the chart inside the <div> element with id="piechart"
      var chart = new google.visualization.PieChart(document.getElementById('piechart'));
      chart.draw(data, options);
}
}

  getBlood(id){
    this.eventService.getBloodInStorage(id).pipe(first()).subscribe(blood => { 
        this.blood = blood; 
        this.init();
    });
}
}
