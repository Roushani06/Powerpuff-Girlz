import mongoose from "mongoose";

const LawyerSchema = new mongoose.Schema({
  name: {
    type: String,
    required: true,
  },
  email: {
    type: String,
    required: true,
    unique: true,
  },
  phone: String,
  password: {
    type: String,
    required: true,
  },
  specialization: String,      // e.g., Criminal, Civil, Family, etc.
  experience: Number,          // in years
  location: String,            // City or State
  bio: String,                 // Short about section
  available: {
    type: Boolean,
    default: true,
  },
  profilePic: String,          // optional
  certificates: [String],      // optional
}, { timestamps: true });

export default mongoose.model("Lawyer", LawyerSchema);
