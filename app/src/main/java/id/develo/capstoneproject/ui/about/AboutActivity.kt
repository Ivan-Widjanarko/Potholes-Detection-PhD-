package id.develo.capstoneproject.ui.about

import androidx.appcompat.app.AppCompatActivity
import android.os.Bundle
import androidx.recyclerview.widget.LinearLayoutManager
import id.develo.capstoneproject.R
import id.develo.capstoneproject.data.CreatorsData
import id.develo.capstoneproject.data.entity.CreatorEntity
import id.develo.capstoneproject.databinding.ActivityAboutBinding

class AboutActivity : AppCompatActivity() {

    private lateinit var binding: ActivityAboutBinding
    private val list: ArrayList<CreatorEntity> = arrayListOf()

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        binding = ActivityAboutBinding.inflate(layoutInflater)
        setContentView(binding.root)

        supportActionBar?.title = "About Us"
        supportActionBar?.setDisplayHomeAsUpEnabled(true)

        list.addAll(CreatorsData.listData)
        val aboutAdapter = AboutAdapter(list)

        with(binding.rvCreators) {
            setHasFixedSize(true)
            layoutManager = LinearLayoutManager(this@AboutActivity)
            adapter = aboutAdapter
        }
    }

    override fun onSupportNavigateUp(): Boolean {
        onBackPressed()
        return true
    }

    override fun onBackPressed() {
        super.onBackPressed()
        finish()
    }
}