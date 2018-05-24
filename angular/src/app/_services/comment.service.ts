import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { User, apiUrl } from '../_models';

@Injectable({
  providedIn: 'root'
})
export class CommentService {

  constructor(private http:HttpClient) { }

  create(comment) {
    return this.http.post(apiUrl+'/api/comment/add/', comment);
}
}
