import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { User, apiUrl,Event, BloodType ,Storage,Message} from '../_models';

@Injectable()
export class EventService {
    constructor(private http: HttpClient) { }

    create(event: Event) {
        return this.http.post(apiUrl+'/api/blood_collection/add/',event);
    }

    getAll() {
      return this.http.get<Event[]>(apiUrl+'/api/blood_collection/add/');
  }

  getAllMessages(id) {
    return this.http.get<Message[]>(apiUrl+'/api/message/get/'+id);
}
  
  getAllStorages() {
    return this.http.get<Storage[]>(apiUrl+'/api/blood_storage/get_storages/');
}
  getBloodInStorage(id){
    return this.http.get<BloodType>(apiUrl+'/api/blood_storage/get_sample_status/'+id+'/');
  }


}