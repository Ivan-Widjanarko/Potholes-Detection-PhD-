package id.develo.capstoneproject

import android.content.Intent
import androidx.appcompat.app.AppCompatActivity
import android.os.Bundle
import com.bumptech.glide.Glide
import id.develo.capstoneproject.databinding.ActivityMainBinding
import id.develo.capstoneproject.ui.about.AboutActivity

class MainActivity : AppCompatActivity() {

    private lateinit var binding: ActivityMainBinding

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        binding = ActivityMainBinding.inflate(layoutInflater)
        setContentView(binding.root)

        startDriving()

        moveToAbout()

        Glide.with(this)
            .load(R.drawable.img_banner)
            .into(binding.imageView)
    }

    private fun startDriving() {
        binding.btnStart.setOnClickListener {
            // DO SOMETHING
        }
    }

    private fun moveToAbout() {
        binding.btnAbout.setOnClickListener {
            Intent(this, AboutActivity::class.java).also {
                startActivity(it)
            }
        }
    }
}