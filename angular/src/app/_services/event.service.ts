import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { User, apiUrl,Event, BloodType } from '../_models';

@Injectable()
export class EventService {
    constructor(private http: HttpClient) { }

    create(event: Event) {
        return this.http.post(apiUrl+'/api/blood_collection/add/',event);
    }

    getAll() {
      return this.http.get<Event[]>(apiUrl+'/api/blood_collection/add/');
  }
  
  getAllStorages(id) {
    return this.http.get<Event[]>(apiUrl+'/api/blood_storage/get_sample_status/'+id+'/');
}
  getBloodInStorage(id){
    return this.http.get<BloodType>(apiUrl+'/api/blood_storage/get_sample_status/'+id+'/');
  }


}