package id.develo.capstoneproject.ui.main

import androidx.appcompat.app.AppCompatActivity
import android.os.Bundle
import com.bumptech.glide.Glide
import id.develo.capstoneproject.R
import id.develo.capstoneproject.databinding.ActivityDrivingBinding

class DrivingActivity : AppCompatActivity() {

    private lateinit var binding: ActivityDrivingBinding

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        binding = ActivityDrivingBinding.inflate(layoutInflater)
        setContentView(binding.root)

        Glide.with(this)
            .load(R.drawable.img_banner)
            .into(binding.imageView)
    }
}