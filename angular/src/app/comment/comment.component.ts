import { Component, OnInit,Input } from '@angular/core';
import { Router, ActivatedRoute } from '@angular/router';
import { FormBuilder, FormGroup, Validators } from '@angular/forms';
import { first } from 'rxjs/operators';
import { fadeAnimation} from '../_animations/fade-in.animation';
import { AlertService, AuthenticationService } from '../_services';
import { CommentService} from '../_services/comment.service';


@Component({
  selector: 'app-comment',
  templateUrl: './comment.component.html',
  styleUrls: ['./comment.component.css']
})
export class CommentComponent implements OnInit {
  commentForm: FormGroup;
  @Input() currentUser;
  constructor(private formBuilder: FormBuilder,private commentService: CommentService,private alertService: AlertService) { }

  ngOnInit() {
    this.commentForm = this.formBuilder.group({
      comment_body: ['', Validators.required],
      user_id: ['']
  });
  }

  // convenience getter for easy access to form fields
  get f() { return this.commentForm.controls; }


  onSubmit() {
    this.commentForm.value.user_id = this.currentUser.user_id;
    console.log(this.commentForm.value);
    // stop here if form is invalid
    if (this.commentForm.invalid) {
        return;
    }

    this.commentService.create(this.commentForm.value)
        .pipe(first())
        .subscribe(
            data => {
              this.commentForm.reset();
              this.alertService.success("Sent!");
            },
            error => {
                this.alertService.error("Error while sending comment");
            });
}

}
