package com.linkedin.frame.exception;

/**
  * This exception is thrown when the feature join is incorrect.
  */
public class FrameFeatureJoinException extends FrameException {

  public FrameFeatureJoinException(ErrorLabel errorLabel, String msg, Throwable cause) {
    super(errorLabel, msg, cause);
  }

  public FrameFeatureJoinException(ErrorLabel errorLabel, String msg) {
    super(errorLabel, msg);
  }
}