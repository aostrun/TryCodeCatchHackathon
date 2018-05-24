import { Component, OnInit } from '@angular/core';
import { EventService } from '../_services/event.service';
import { FormBuilder, FormGroup, Validators } from '@angular/forms';
import {NgbModule} from '@ng-bootstrap/ng-bootstrap';
import { first } from 'rxjs/operators';

declare const google: any;

@Component({
  selector: 'app-event',
  templateUrl: './event.component.html',
  styleUrls: ['./event.component.css']
})



export class EventComponent implements OnInit {

  eventForm: FormGroup;
    submitted = false;
    lat: any;
    long: any;

  constructor(public eventService: EventService,private formBuilder: FormBuilder) { }

  ngOnInit() {

    let mapProp = {
            center: new google.maps.LatLng(45.815399, 15.966568),
            zoom: 10,
            mapTypeId: google.maps.MapTypeId.ROADMAP
        };
        let map = new google.maps.Map(document.getElementById("googleMap"), mapProp);
        var marker;
        var self = this;
         map.addListener('click', function(e) {
            var str = placeMarkerAndPanTo(e.latLng, map);
            
            var stra = str.split("-");
            
            self.lat= stra[0];
            self.long = stra[1];

          });

        function placeMarkerAndPanTo(latLng, map) {
            if (marker != undefined){
                marker.setMap(null);
            }
            marker = new google.maps.Marker({
              position: latLng,
              map: map
            });
            var ll = JSON.stringify(latLng);
            var ll2 = JSON.parse(ll);

            var lat = ll2.lat;
            var long = ll2.lng;
            
            map.panTo(latLng);
            var str = ""+lat+"-"+""+long;
            return str;
          }



    this.eventForm = this.formBuilder.group({
      name: ['', Validators.required],
      start_time: ['', Validators.required],
      end_time: ['', Validators.required],
      location_lat: ['',] ,
      location_lon: ['',],
      storage: ['']
  });


  }


   // convenience getter for easy access to form fields
   get f() { return this.eventForm.controls; }

   onSubmit() {
       this.submitted = true;
      
      this.eventForm.value.location_lat = this.lat;
        this.eventForm.value.location_lon = this.long;
        this.eventForm.value.storage = 1;

        
        console.log(this.eventForm.value);
       // stop here if form is invalid
       if (this.eventForm.invalid) {
           return;
       }
       

       this.eventService.create(this.eventForm.value)
           .pipe(first())
           .subscribe(
               data => {
                   console.log("created");
               },
               error => {
                   alert("error");
               });
   }

}
