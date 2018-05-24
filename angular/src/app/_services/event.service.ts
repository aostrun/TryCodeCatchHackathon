import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { User, apiUrl,Event, BloodType ,Storage,Message} from '../_models';

@Injectable()
export class EventService {
    constructor(private http: HttpClient) { }

    getAll() {
      return this.http.get<Event[]>(apiUrl+'/api/blood_collection/get_valid/');
  }

  getAllMessages(id) {
    return this.http.get<Message[]>(apiUrl+'/api/message/get_unread/'+id);
}

deleteMessage(id) {
  return this.http.get<Message>(apiUrl+'/api/message/mark_as_read/'+id);
}

sendMessage(msg){
  return this.http.post(apiUrl+'/api/message/add/',msg);
}
  
  getAllStorages() {
    return this.http.get<Storage[]>(apiUrl+'/api/blood_storage/get_storages/');
}
  getBloodInStorage(id){
    return this.http.get<BloodType>(apiUrl+'/api/blood_storage/get_sample_status/'+id+'/');
  }


}