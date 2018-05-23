import { Component, OnInit } from '@angular/core';
import { Router } from '@angular/router';
import { FormBuilder, FormGroup, Validators, AbstractControl } from '@angular/forms';
import { first } from 'rxjs/operators';
import { AlertService, UserService } from '../_services';
import * as Typed from "typed.js"

declare const google: any;

@Component({templateUrl: 'register.component.html'
})
export class RegisterComponent implements OnInit {
    registerForm: FormGroup;
    loading = false;
    submitted = false;
    typed: any;
    lat: any;
    long: any;

    constructor(
        private formBuilder: FormBuilder,
        private router: Router,
        private userService: UserService,
        private alertService: AlertService) { }

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

        this.makeMessage("Join us");
          /*
        this.registerForm = this.formBuilder.group({
            first_name: ['', Validators.required],
            last_name: ['', Validators.required],
            username: ['', Validators.required],
            email: ['', [Validators.required, Validators.email]],
            password1: ['', [Validators.required, Validators.minLength(8)]],
            password2: ['', [Validators.required, Validators.minLength(8)]],
            number: ['', Validators.required],
            date: ['', Validators.required],
            sex: ['', Validators.required],
            location_lat: [''],
            location_lon: [''],
            blood_type:['']
        },{
            validator: [PasswordValidation.MatchPassword,NumberValidation.Number] //confirm password same as password
        });
        */
        this.registerForm = this.formBuilder.group({
            first_name: ['', ],
            last_name: ['', ],
            username: ['', ],
            email: ['', ],
            password1: ['', ],
            password2: ['', ],
            number: ['', ],
            date: ['', ],
            sex: ['', ],
            location_lat: [''],
            location_lon: [''],
            blood_type:['']
        });
    }

    // convenience getter for easy access to form fields
    get f() { return this.registerForm.controls; }



    onSubmit() {
        this.submitted = true;
        console.log(this.lat);
        this.registerForm.value.location_lat = this.lat;
        this.registerForm.value.location_lon = this.long;

        
        // stop here if form is invalid
        if (this.registerForm.invalid) {
            return;
        }
        console.log(this.registerForm.value);
        this.loading = true;
        this.userService.create(this.registerForm.value)
            .pipe(first())
            .subscribe(
                data => {
                    this.alertService.success('Registration successful', true);
                    this.router.navigate(['/login']);
                },
                error => {
                    this.alertService.error(error);
                    this.loading = false;
                });
    }



    makeMessage(newTexts: String){
          
        const dataType = newTexts;   // 

        if (dataType === undefined) {
          return false;
        }
        const strings = dataType.split(',');

        if(this.typed && this.typed.constructor === Typed) {
            this.typed.destroy();
        }

        this.typed = new Typed("#register_text", {
          strings: strings,
          typeSpeed: 70,
          showCursor: false
        });
    }




  
}

export class PasswordValidation {

    static MatchPassword(AC: AbstractControl) {
       let password = AC.get('password1').value; // to get value in input tag
       let confirmPassword = AC.get('password2').value; // to get value in input tag
        if(password != confirmPassword) {
            AC.get('password2').setErrors( {MatchPassword: true} )
        } else {
            return null
        }
    }
}

export class NumberValidation {

    static Number(AC: AbstractControl) {
       let number = AC.get('number').value; // to get value in input tag
        if(isNaN(number)) {
            AC.get('number').setErrors( {WronNumber: true} )
        } else {
            return null
        }
    }

 


}
