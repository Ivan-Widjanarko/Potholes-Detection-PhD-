package id.develo.capstoneproject.ui.main

import android.content.Intent
import androidx.appcompat.app.AppCompatActivity
import android.os.Bundle
import android.view.View
import android.widget.Toast
import androidx.activity.viewModels
import com.bumptech.glide.Glide
import id.develo.capstoneproject.R
import id.develo.capstoneproject.databinding.ActivityDrivingBinding
import id.develo.capstoneproject.ui.report.ReportActivity
import id.develo.capstoneproject.utils.AppPreferences

class DrivingActivity : AppCompatActivity() {

    private lateinit var binding: ActivityDrivingBinding

    private val drivingViewModel: MainDrivingViewModel by viewModels()

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        binding = ActivityDrivingBinding.inflate(layoutInflater)
        setContentView(binding.root)

        // Set progress bar if start button is clicked.
        setProgressBar()

        drivingViewModel.isSuccess.observe(this, {
            if (it) {
                Intent(this, ReportActivity::class.java).also { intent ->
                    startActivity(intent)
                }
            }
        })

        binding.btnStop.setOnClickListener {
            if (AppPreferences.isLogin) {
                drivingViewModel.setState(AppPreferences.uId, 0)
            }
        }

        Glide.with(this)
            .load(R.drawable.img_banner)
            .into(binding.imageView)
    }

    private fun setProgressBar() {
        drivingViewModel.isLoading.observe(this, {
            binding.progressBar.visibility = if (it) View.VISIBLE else View.GONE
        })
    }

    override fun onBackPressed() {
//        super.onBackPressed()
        Toast.makeText(this, "Please stop first to go back.", Toast.LENGTH_SHORT).show()
        return
    }
}