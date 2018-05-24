import { Component, OnInit,Input} from '@angular/core';
import { User, Event,BloodType,Storage ,Message, BLOOD_TYPES} from '../_models';
import { EventService } from '../_services/event.service';
import { first } from 'rxjs/operators';
import * as Typed from "typed.js";
import { UserService, AlertService } from '../_services';

declare var google:any;

@Component({
  selector: 'app-home-body',
  templateUrl: './home-body.component.html',
  styleUrls: ['./home-body.component.css']
})
export class HomeBodyComponent implements OnInit {
  @Input() currentUser: User;
  users: User[] = [];
  blood: BloodType;
  blood_types = BLOOD_TYPES;
  selected_blood_type:string;
   storages: Storage[] = [];
  events: Event[]=[];
  map: any;
  marker: any;
  active: Event;


  constructor(private eventService: EventService,private userService: UserService,private alertService: AlertService) { }

  ngOnInit() {

 

    

    this.loadAllEvents();
    this.loadAllStorages();
    
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
      var options = {'title':'Blood storage', 'width':400, 'height':400};
    
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

private loadAllEvents() {
  this.eventService.getAll().pipe(first()).subscribe(events => { 
      this.events = events; 

    let mapProp = {
        center: new google.maps.LatLng(45.815399, 15.966568),
        zoom: 11,
        mapTypeId: google.maps.MapTypeId.ROADMAP
    };
    this.map = new google.maps.Map(document.getElementById("googleMap"), mapProp);

 
    

      
  });
}

setMarker(e){
  if (this.marker != undefined){
    this.marker.setMap(null);
}
  this.active = e;

  this.marker = new google.maps.Marker({
    position: {lat: e.location_lat, lng: e.location_lon},
    map: this.map
  });
}

private loadAllStorages() {
  this.eventService.getAllStorages().pipe(first()).subscribe(storages => { 
      this.storages = storages; 
      
  });
}

getSelected(value){
  this.selected_blood_type = value;
}

updateBlood(){
  this.userService.update({blood_type: this.selected_blood_type}).pipe(first()).subscribe(blood => { 
    this.currentUser.blood_type = this.selected_blood_type;
    alert("Blood type updated!");
});
}

}
